class HomePageData:
    test_home_data = [  # Data for single product tests
        {
            "test_name": "test_phone_search",
            "search_term": "iPhone 14",
            "target_product_title": "Apple iPhone 15"
        },
        {
            "test_name": "test_laptop_search",
            "search_term": "HP 15",
            "target_product_title": "HP 15, 13th Gen Intel Core i5-1334U"
        },
        # ... more single product data
    ]

    # Data for multiple product tests
    test_home_data_multiple = [
        [  # Test run 1 (2 products)
            {"search_term": "iPhone 14", "target_product_title": "Apple iPhone 14"},
            {"search_term": "Laptop", "target_product_title": "HP Laptop"}
        ],
    [  # Test run 3 (2 products)
        {"search_term": "Tablet", "target_product_title": "Lenovo Tab"},
        {"search_term": "Smartwatch", "target_product_title": "Noise Pulse 2"}
    ]
    ]