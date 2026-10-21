import os
import requests
from bs4 import BeautifulSoup
from google import genai

# ১. ডেটা এক্সট্রাকশন লেয়ার (Data Extraction Layer)
def fetch_market_context(url):
    """নির্দিষ্ট ওয়েবসাইট থেকে টেক্সট ডেটা স্ক্র্যাপ করার মেকানিズム।"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # ওয়েবসাইটের প্যারাগ্রাফগুলো থেকে ডেটা ফিল্টার করা
            paragraphs = soup.find_all('p')
            context = " ".join([p.text for p in paragraphs[:5]]) # প্রথম ৫টি প্যারাগ্রাফ নেওয়া হলো
            return context if context.strip() else "Error: No text content found on the page."
        else:
            return f"Error: Unable to fetch data. Status code: {response.status_code}"
    except Exception as e:
        return f"Error: Connection failed. {str(e)}"

# ২. সিলিকন ইন্টেলিজেন্স লেয়ার (AI Synthesis Layer)
def analyze_with_ai(market_data):
    """গুগল জেমিনি এপিআই ব্যবহার করে র র ডেটাকে লজিক্যাল ইনসাইটে রূপান্তর।"""
    # নোট: আপনার এনভায়রনমেন্ট ভ্যারিয়েবলে GEMINI_API_KEY সেট থাকতে হবে
    client = genai.Client()
    
    prompt = f"""
    You are an advanced Secular Economic Physics AI. Analyze the following raw market data.
    Provide a hyper-logical, sugarcoating-free summary highlighting:
    1. Core Economic Disruption (The main event)
    2. Efficiency vs Waste Index (Where energy/capital is being lost or optimized)
    3. Future Probabilistic Trend (Next logical step in the matrix)
    
    Raw Data: {market_data}
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    return response.text

# ৩. এক্সিকিউশন নোড (Execution Node)
if __name__ == "__main__":
    # টেস্ট করার জন্য একটি গ্লোবাল ইকোনমিক নিউজ বা ফাইন্যান্সিয়াল লিংক
    target_url = "https://www.bbc.com/news/business" 
    
    print("[*] Shifting energy to data extraction...")
    raw_data = fetch_market_context(target_url)
    
    if "Error" not in raw_data:
        print("[*] Data locked. Initializing Silicon Intelligence layer...")
        analysis = analyze_with_ai(raw_data)
        print("\n=== SYSTEM LOGICAL OUTPUT ===")
        print(analysis)
    else:
        print(raw_data)
