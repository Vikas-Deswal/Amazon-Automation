# Amazon UI Automation Framework

[![Run Selenium Smoke Tests](https://github.com/Vikas-Deswal/Amazon-Automation/actions/workflows/run-tests.yml/badge.svg)](https://github.com/Vikas-Deswal/Amazon-Automation/actions/workflows/run-tests.yml)

> **Selenium-based UI test automation framework demonstrating Page Object Model, data-driven testing, and clean test architecture for e-commerce workflows.**

## Project Scope & Focus

**This project demonstrates:**
- **Languages**: Python 3.10+
- **Frameworks**: pytest, Selenium WebDriver 4.x
- **Design Patterns**: Page Object Model (POM)
- **Testing Approaches**: Data-driven testing, Parametrization
- **Reporting**: Allure Reports with detailed step logging
- **CI/CD**: GitHub Actions for automated test execution
- **Version Control**: Git with clean commit history


## Architecture Highlights

- **Design Pattern:** Page Object Model with clear separation of concerns
- **Test Framework:** pytest with custom fixtures for setup/teardown
- **Reporting:** Allure Reports with step-by-step test execution details
- **Test Data Management:** Centralized data files for easy maintenance
- **Logging:** Custom logger utility for debugging and traceability
- **Browser Support:** Chrome (extensible to Firefox, Edge)

## Test Coverage

This framework covers the following e-commerce user journeys:

| Feature | Test Scenarios | Status |
|---------|---------------|--------|
| **Search** | Search box validation, product search | Automated |
| **Product Details** | Title, price, ratings, images validation | Automated |
| **Cart Operations** | Add to cart, quantity modification, removal | Automated |
| **Multi-Product Flow** | Add multiple products, cart total validation | Automated |
| **Price Validation** | Cart subtotal, item-level pricing | Automated |

## Test Reporting

This framework generates comprehensive **Allure Reports** with:
- Step-by-step test execution details
- Screenshots and attachments for each test step
- Test history and trend analysis
- Categorized by Epic, Feature, and Story
- Pass/Fail statistics with severity levels

**Example Report Output:**
```
✅ 8 tests passed
⏱️ Execution time: ~20-30 seconds (parallel mode)
📊 Coverage: End-to-end e-commerce workflows
```

To view the report locally:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Repository Structure

```text
Amazon-Automation/
├── pageObjects/           
│   ├── HomePage.py        
│   ├── SearchResults.py   
│   ├── Products.py        
│   └── addToCart.py       
├── tests/                 
│   ├── conftest.py        
│   ├── test_single_product_add_to_cart.py    
│   └── test_add_multiple_products_to_cart.py 
├── TestData/              
│   └── HomePage_Data.py   
├── utilities/             
│   ├── logging.py         
│   └── PriceOperations.py 
├── reports/               
├── allure-results/      
├── requirements.txt       
└── README.md
```

## Quick Start

```bash
git clone https://github.com/yourusername/Amazon-Automation.git
cd Amazon-Automation
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest --alluredir=allure-results
allure serve allure-results
```

## Key Metrics

- **Test Count**: 8 test cases covering critical e-commerce workflows
- **Execution Time**: ~60-90 seconds per test run (sequential with anti-bot delays)
- **Pass Rate**: 100% (when Amazon UI is stable)
- **Test Coverage**: End-to-end user journeys (search → product details → cart operations)
- **CI/CD**: Automated on every push to main branch

## Getting Started

### Prerequisites

- **Python**: 3.10+
- **Google Chrome**: Latest stable version
- **ChromeDriver**: Managed automatically by Selenium 4.6+ (no manual download needed)
- **Allure**: For generating test reports

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Amazon-Automation
   ```

2. **Create and activate virtual environment** (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # On Windows: .venv\Scripts\activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Allure** (for report generation)
   ```bash
   # macOS (using Homebrew)
   brew install allure
   
   # Windows (using Scoop)
   scoop install allure
   
   # Linux (manual installation)
   # Download from: https://github.com/allure-framework/allure2/releases
   ```

## Running Tests

### Basic Execution

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_single_product_add_to_cart.py

# Run specific test class
pytest tests/test_single_product_add_to_cart.py::TestAdd_Single_Product_to_Cart

# Run specific test method
pytest tests/test_single_product_add_to_cart.py::TestAdd_Single_Product_to_Cart::test_homepage
```

### Test Reporting

```bash
# Generate HTML report
pytest --html=reports/report.html

# Generate Allure report
pytest --alluredir=allure-results
allure serve allure-results

# View existing Allure report
allure generate allure-results --clean -o allure-report
allure open allure-report
```

### Parallel Execution (Local Development)

```bash
# Install pytest-xdist for parallel execution
pip install pytest-xdist

# Run tests in parallel
pytest -n 4 --alluredir=allure-results

# Auto-detect number of CPU cores
pytest -n auto --alluredir=allure-results

# Run with verbose output and parallel execution
pytest -n 4 -v --alluredir=allure-results
```

**Note:** Parallel execution reduces test suite runtime from ~60 seconds to ~20-30 seconds (depending on system resources).

## CI/CD Pipeline

This project includes **GitHub Actions** for automated test execution:

### Automatic Execution
- Tests run automatically on every push to the `main` branch
- Generates Allure reports and uploads as artifacts
- **Sequential execution** used to avoid Amazon's anti-bot detection
- Built-in delays between requests to respect rate limits

### Manual Trigger
- Go to **Actions** tab in GitHub
- Select **Run Selenium Smoke Tests** workflow
- Click **Run workflow** button
- Choose browser (Chrome/Firefox/Edge) and headless mode (true/false)
- Tests execute with your selected configuration

### View Results
- Download **allure-report** artifact from workflow run
- Extract and open `index.html` in browser to view detailed test report

## Test Data Management

Test data is centralized in `TestData/HomePage_Data.py` for easy maintenance and reusability.

### Data Structure

```python
# Single product test data
test_home_data = [
    {
        "test_name": "test_phone_search",
        "search_term": "iPhone 14",
        "target_product_title": "Apple iPhone 15"
    },
    # ... more products
]

# Multiple product test data
test_home_data_multiple = [
    [
        {"search_term": "iPhone 14", "target_product_title": "Apple iPhone 14"},
        {"search_term": "Laptop", "target_product_title": "HP Laptop"}
    ],
    # ... more product combinations
]
```

### Customization

To test different products, simply update the data in `TestData/HomePage_Data.py`:
- **search_term**: Product keyword to search
- **target_product_title**: Expected product title in results

## Detailed Test Cases

### Single Product Workflow (`TestAdd_Single_Product_to_Cart`)

| Test Case | Severity | Description |
|-----------|----------|-------------|
| `test_search_box_present` | Normal | Validates search box visibility on home page |
| `test_homepage` | Critical | Performs product search and navigates to results |
| `test_search_results` | Critical | Locates target product and opens detail page |
| `test_product_overview` | Critical | Validates product title, price, ratings, images |
| `test_add_to_cart` | Blocker | Adds product to cart and verifies pricing |
| `test_add_quantity_cart` | Critical | Increases quantity and validates cart total |
| `test_reduce_cart_quantity` | Normal | Decreases quantity in cart |
| `test_delete_cart_quantity` | Critical | Removes product and verifies cart is empty |

### Multiple Product Workflow (`TestAdd_Multiple_Products_to_Cart`)

| Test Case | Severity | Description |
|-----------|----------|-------------|
| `test_add_multiple_to_cart` | Critical | Adds multiple products sequentially and validates final cart state |

## Key Design Decisions & Learnings

### Why Page Object Model?
- **Maintainability**: UI changes require updates in one place only
- **Reusability**: Page methods can be reused across multiple tests
- **Readability**: Tests read like user stories, not technical code

### Why pytest?
- **Powerful fixtures**: Setup/teardown with scope control
- **Parametrization**: Data-driven testing with minimal code
- **Rich ecosystem**: Extensive plugin support (pytest-html, allure-pytest)

### Why Allure Reports?
- **Stakeholder-friendly**: Non-technical users can understand test results
- **Detailed steps**: Each test action is logged with attachments
- **Historical trends**: Track test stability over time

### Why Centralized Test Data?
- **Single source of truth**: All test data in one location
- **Easy updates**: Change product searches without touching test code
- **Scalability**: Add new test scenarios by adding data entries

## Known Limitations & Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| **Locator failures** | Amazon UI changes frequently | Update XPath/CSS selectors in `pageObjects/` |
| **Timeout errors** | Slow network or page load | Increase wait times in `WebDriverWait` calls |
| **ChromeDriver issues** | Version mismatch | Selenium 4.6+ auto-manages drivers; ensure Chrome is updated |
| **Test flakiness** | Dynamic content loading | Add explicit waits for element visibility |

### Best Practices

- **Run tests in isolation**: Each test should be independent
- **Use explicit waits**: Avoid `time.sleep()` for stability
- **Keep test data updated**: Amazon product availability changes
- **Review Allure reports**: Analyze failures with screenshots and logs

## Potential Extensions

This framework can be extended to support:

- **Cross-browser testing** (Firefox, Edge, Safari)
- **Headless execution** for faster CI/CD runs
- **Screenshot on failure** for better debugging
- **Visual regression testing** (Percy/Applitools)
- **Accessibility testing** (axe-core/WCAG compliance)
- **Mobile responsive testing** (Appium/BrowserStack)
- **Database validation** for order verification

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author
**Vikas Deswal**