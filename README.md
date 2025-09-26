# Amazon-Automation

Automation test suite built with `pytest` and Selenium to cover key Amazon shopping journeys (search, product validation, cart management) for both single and multiple product flows. The suite follows the Page Object Model and uses centralized test data from `TestData/HomePage_Data.py`.

## Repository structure

```text
Amazon-Automation/
├── pageObjects/           # Page Object Model classes for each Amazon page
├── tests/                 # Pytest suites for single and multi-product scenarios
├── TestData/              # Centralized data used by fixtures and tests
├── utilities/             # Logger and helper utilities
├── reports/               # HTML/pytest reports (auto-created)
├── requirements.txt       # Python dependencies
└── README.md
```

## Getting the code

- **Clone a fresh copy**
  ```bash
  git clone <repository-url>
  cd Amazon-Automation
  ```

- **Pull the latest changes** (from `main`; update the branch name if different)
  ```bash
  git pull origin main
  ```

## Prerequisites

- **Python**: 3.10+ (developed against CPython; create a virtual environment if desired)
- **Google Chrome**: Latest stable version installed locally
- **ChromeDriver**: Managed automatically by Selenium 4.6+ via Selenium Manager; no manual download required in most environments

## Install dependencies

- **Install requirements**
  ```bash
  pip install -r requirements.txt
  ```

If you prefer isolation, create and activate a virtual environment before installing dependencies:

```bash
python -m venv .venv
source .venv/bin/activate    # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running the tests

- **Execute the full suite**
  ```bash
  pytest
  ```

- **Run a specific module**
  ```bash
  pytest tests/test_single_product_add_to_cart.py
  ```

- **Generate an HTML report**
  ```bash
  pytest --html reports/<filename>.html
  ```

- **Headless execution (optional)**
  Add a custom option in `tests/conftest.py` to initialize `webdriver.Chrome(options=...)` with headless arguments if needed.

## Test data management

- **Single-product scenarios** load from `HomePageData.test_home_data`.
- **Multi-product scenarios** iterate over `HomePageData.test_home_data_multiple`.
- Update the search terms or expected titles in `TestData/HomePage_Data.py` to run the flow against different products.

## Covered test cases

| Test class (`tests/`) | Test case | Description |
| --- | --- | --- |
| `TestAdd_Single_Product_to_Cart` | `test_search_box_present` | Verifies that the Amazon home page exposes the search box. |
|  | `test_homepage` | Submits a search term from data and navigates to search results. |
|  | `test_search_results` | Locates the desired product from results and opens its detail page. |
|  | `test_product_overview` | Confirms product title, price, ratings, and images are present. |
|  | `test_add_to_cart` | Adds the product to the cart and checks pricing in the subtotal widget. |
|  | `test_add_quantity_cart` | Increments cart quantity and validates totals. |
|  | `test_reduce_cart_quantity` | Decrements cart quantity to the previous value. |
|  | `test_delete_cart_quantity` | Removes the product from the cart and verifies the removal confirmation. |
| `TestAdd_Multiple_Products_to_Cart` | `test_add_multiple_to_cart` | Loops through multiple products, adds each to the cart, validates titles and prices, and verifies the final cart. |

## Notes & troubleshooting

- **Locator updates**: Amazon UI changes frequently. If locators in `pageObjects/` no longer match the live site, update them to restore stability.
- **Slow networks**: Consider adding explicit waits (e.g., Selenium `WebDriverWait`) for reliability if the site is slow to load.
- **Reports directory**: Ensure the `reports/` directory exists or allow `pytest` to create it when generating HTML output.

## Contributing

- Fork the repository and create feature branches for significant updates.
- Open pull requests with descriptive change logs and mention any new test data required.
