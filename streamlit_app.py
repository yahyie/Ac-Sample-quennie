import streamlit as st

# Sample food items
food_items = {
    "Pizza": {"price": 8.99, "image": "https://media.istockphoto.com/id/938742222/photo/cheesy-pepperoni-pizza.jpg?s=612x612&w=0&k=20&c=D1z4xPCs-qQIZyUqRcHrnsJSJy_YbUD9udOrXpilNpI="},
    "Burger": {"price": 5.99, "image": "https://via.placeholder.com/150"},
    "Pasta": {"price": 7.99, "image": "https://via.placeholder.com/150"},
    "Salad": {"price": 4.99, "image": "https://via.placeholder.com/150"},
}

# Initialize session state for cart
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# Function to add item to cart
def add_to_cart(item_name):
    if item_name in st.session_state.cart:
        st.session_state.cart[item_name] += 1
    else:
        st.session_state.cart[item_name] = 1

# Function to remove item from cart
def remove_from_cart(item_name):
    if item_name in st.session_state.cart:
        del st.session_state.cart[item_name]

# Function to calculate total price
def calculate_total():
    total = 0
    for item, quantity in st.session_state.cart.items():
        total += food_items[item]["price"] * quantity
    return total

# Streamlit app layout
st.title("Food Ordering System")

# Display food items
st.header("Menu")
for item, details in food_items.items():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image(details["image"], caption=item)
        st.write(f"Price: ${details['price']:.2f}")
        if st.button(f"Add {item} to Cart"):
            add_to_cart(item)
            st.success(f"{item} added to cart!")

# Display cart
st.header("Your Cart")
if st.session_state.cart:
    for item, quantity in st.session_state.cart.items():
        st.write(f"{item}: {quantity} x ${food_items[item]['price']:.2f} = ${quantity * food_items[item]['price']:.2f}")
        if st.button(f"Remove {item} from Cart"):
            remove_from_cart(item)
            st.experimental_rerun()
    
    total_price = calculate_total()
    st.write(f"Total Price: ${total_price:.2f}")
    
    if st.button("Checkout"):
        st.success("Thank you for your order!")
        st.session_state.cart.clear()
else:
    st.write("Your cart is empty.")

# Footer
st.write("Made with ❤️ by Your Name")
