# Tunisian Real Estate EstateMind Scraper 🚀

EstateMind is a high-performance, automated real estate data harvesting engine designed to map the Tunisian property market.

## 🛠 Project Architecture
The system follows a 3-stage pipeline to ensure data completeness and quality:

### 1. 🔍 Crawling (Discovery Stage)
The engine recursively discovers the Tunisian real estate ecosystem.
- **Deep Discovery**: Uses SerpAPI to paginate through Google results for regional keywords (e.g., "agence immobilière Sousse").
- **Exhaustive Mapping**: Scans for `sitemap.xml` and DNS records (`crt.sh`) to find niche agencies that are normally hidden.
- **Quality Score**: Every discovered site is validated for relevance before being added to the target list.

### 2. ✂️ Scraping (Extraction Stage)
Once a target is validated, the scraper dives deep into the property categories.
- **Specialized Engines**: Custom logic for major platforms like `Mubawab.tn` and `MenZili.tn`.
- **Heuristic Generic Scraper**: A robust fallback system that automatically extracts titles, prices, and images from any real estate site using BS4.
- **Data Normalization**: Cleans and validates prices, surfaces, and locations to ensure a uniform dataset.

### 3. 💾 Data Storage (MongoDB Integration)
All extracted data is synced in real-time to a Cloud database.
- **MongoDB Atlas**: Fully persistent storage allowing for complex queries and analysis.
- **Deduplication**: Uses data hashing to ensure no property is ever saved twice, even across multiple runs.
- **Excel Export**: For every cycle, a fresh `final_listings_report.xlsx` is generated for instant business use.

## 🚀 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Configure `.env` (use `.env.example` as a template).
3. Run the engine: `python main.py`

*Note: The system is designed to run on a 24-hour cycle automatically.*
