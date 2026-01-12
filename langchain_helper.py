from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os
from google_secret import key

os.environ["GOOGLE_API_KEY"] = key


primary_llm = ChatGoogleGenerativeAI(model="gemini-3-pro-preview", max_retries=0)

# 2. THE FALLBACKS: Ordered from smartest to most available
fallbacks = [
    # Intelligent and fast (2026 workhorse)
    ChatGoogleGenerativeAI(model="gemini-3-flash-preview"),
    
    # Highly stable previous-gen high-tier
    ChatGoogleGenerativeAI(model="gemini-2.5-pro"),
    
    # Excellent balance of speed and intelligence
    ChatGoogleGenerativeAI(model="gemini-2.0-flash"),
    
    # High Quota (1,000 requests/day) - Your current "safe" floor
    ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite"),
    
    # LEGACY STABLE: Older but very reliable for simple tasks
    ChatGoogleGenerativeAI(model="gemini-1.5-flash"),
    
    # ULTRA-LIGHT: The fastest/smallest model for basic automation
    ChatGoogleGenerativeAI(model="gemini-1.5-flash-8b")
]

# 3. COMBINE: Create the final resilient object
llm = primary_llm.with_fallbacks(fallbacks)

def generateRestaurantName(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to make a {cuisine} Restaurant. Suggest me a good name for it. Respond with a name only.",
    )

    name_chain = prompt_template_name | llm | StrOutputParser()

    prompt_template_items = PromptTemplate(
        input_variables=["RestaurantName"],
        template="Suggest me some popular dishes for a restaurant named {RestaurantName}. Respond with a comma separated list only."
    )

    items_chain = prompt_template_items | llm | StrOutputParser()
    full_chain = (
        {"RestaurantName": name_chain} 
        | RunnablePassthrough.assign(PopularDishes=items_chain)
    )

    # --- 4. Invoke and Print ---
    response = full_chain.invoke({"cuisine": cuisine})
    return response
