try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found. Please install it using 'pip install google'")




def google_search(query):
    try:
        for j in search(query, num=10, stop=10, pause=2):
            print(j)
    except Exception as e:
        print(e)
while True:
    user_input = input("Enter a number (0 to exit) or write your query: ")

    if user_input == "0":
        print("Exiting the program.")
        break  
    if __name__ == "__main__":
        query =user_input
        google_search(query)
 
    print(f"You entered: {user_input}")

