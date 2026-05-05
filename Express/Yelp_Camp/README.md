# 🏕️ YelpCamp

YelpCamp is a full-stack web application that allows users to discover, create, review, and manage campgrounds. It focuses on building a complete CRUD-based platform with authentication, authorization, and real-world backend workflows.

---

## 🚀 Features

- 🔐 User Authentication (Register / Login / Logout)  
- 🏕️ Create, Edit, and Delete Campgrounds  
- 📝 Add and Manage Reviews  
- ⭐ Rating system for campgrounds  
- 🛡️ Authorization (only owners can edit/delete)  
- 🌍 Interactive maps & location display  
- ☁️ Image upload and storage  
- ⚠️ Error handling and validation  

---

## 🧱 Tech Stack

### 🎨 Frontend
- HTML, CSS, Bootstrap  
- EJS (Embedded JavaScript Templates)  

### ⚙️ Backend
- Node.js  
- Express.js  

### 🗄️ Database
- MongoDB (via Mongoose)  

### 🔧 Other Tools & Services
- Cloudinary (image uploads)  
- Mapbox (maps & geolocation)  
- Passport.js (authentication)  
- Joi (validation)  

---

## 📂 Project Structure

```
/models        → Mongoose schemas  
/routes        → Express route handlers  
/controllers   → Business logic separation  
/views         → EJS templates  
/public        → Static assets (CSS, JS)  
/utils         → Custom error handling  
/middleware    → Auth & validation middleware  
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```
git clone https://github.com/yelloworld-code/Yelp_Camp.git
cd Yelp_Camp
```

### 2. Install dependencies
```
npm install
```

### 3. Setup environment variables

Create a `.env` file in the root:

```
DB_URL=your_mongodb_connection  
CLOUDINARY_CLOUD_NAME=your_cloud_name  
CLOUDINARY_KEY=your_key  
CLOUDINARY_SECRET=your_secret  
MAPBOX_TOKEN=your_mapbox_token  
SECRET=session_secret  
```

---

### ▶️ Run the app
```
node app.js
```

Visit:
```
http://localhost:3000
```

---

## 🔐 Authentication Flow

- Users must register/login to create campgrounds or reviews  
- Authorization ensures only the owner can edit/delete their content  
- Sessions are handled using Passport.js  

---

## 🧠 Key Learnings

- Structuring a scalable Express application  
- Implementing authentication & authorization  
- Handling file uploads and external APIs  
- Writing reusable middleware  
- Managing full CRUD operations with MongoDB  

---

## 📌 Future Improvements

- Refactor to React / Next.js frontend  
- Add search & filtering system  
- Improve UI/UX design (modern interface)  
- Add pagination and performance optimizations  
- Role-based access control (admin panel)  

---

## 🙌 Acknowledgements

This project is inspired by learning full-stack development concepts and building real-world applications using the MERN ecosystem.

---

## 📄 License

This project is for educational purposes.
