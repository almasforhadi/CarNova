# 🚗 CarNova

**CarNova** is a fully functional car sales web application built with Django. It allows users to browse and filter car listings, register and manage accounts, purchase cars, and view their order history.

---

## 🧩 Features

### 🛍️ Car Listings
- View a list of cars with images, titles, descriptions, and prices.
- Filter cars by brand name.
- View detailed car pages with full information.
- Add public comments to any car.

### 👤 User Accounts
- User registration and login/logout.
- Authenticated navigation menu (Home, Profile, Logout).
- Unauthenticated navigation menu (Home, Signup, Login).
- Users can update/edit their profile details.

### 🛒 Purchase System
- Authenticated users can buy cars using a "Buy Now" button.
- Car quantity decreases after each purchase.
- Unauthenticated users cannot see or access the "Buy Now" button.

### 📦 Order History
- Authenticated users can view their personal order history on the profile page.

---

## 🏗️ Tech Stack

- **Backend:** Django
- **Database:** SQLite (default Django database)
- **Frontend:** HTML, CSS, Bootstrap (optional)
- **Image Handling:** Pillow for image uploads

---