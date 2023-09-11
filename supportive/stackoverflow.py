import requests

def search_stack_overflow(query):
    base_url = "https://api.stackexchange.com/2.2/search/advanced"
    params = {
        "site": "stackoverflow",
        "order": "relevance",
        "sort": "relevance",
        "q": query,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("items", [])
    else:
        return []

if __name__ == "__main__":
    query = input("Enter your question: ")
    
    results = search_stack_overflow(query)
    
    if not results:
        print("No results found.")
    else:
        print("\nSearch Results:")
        for i, result in enumerate(results, start=1):
            print(f"{i}. {result['title']}")

        selection = input("Enter the number to view the selected result (or 'q' to quit): ")
        while selection != 'q':
            if selection.isdigit() and 1 <= int(selection) <= len(results):
                selected_result = results[int(selection) - 1]
                print(f"Link to the selected result: {selected_result['link']}")
            else:
                print("Invalid selection. Please enter a valid number or 'q' to quit.")

            selection = input("Enter the number to view the selected result (or 'q' to quit): ")
