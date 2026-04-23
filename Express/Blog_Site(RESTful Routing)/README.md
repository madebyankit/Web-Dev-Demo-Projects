# RESTful Blog Site

A full-stack blog application built with Express.js, MongoDB, and EJS templating. Implements RESTful routing for CRUD operations on blog posts.

## Features

- **Create Blog Posts**: Add new blog entries with title, image URL, and content
- **Read Blog Posts**: View all posts on the index page and individual posts in detail
- **Update Blog Posts**: Edit existing posts with a user-friendly form
- **Delete Blog Posts**: Remove posts from the database
- **RESTful Routing**: Follows REST conventions for all CRUD operations
- **Input Sanitization**: Protects against XSS attacks using express-sanitizer
- **Responsive Design**: Uses Semantic UI for clean, mobile-friendly interface

## Technologies Used

- **Express.js**: Web framework for Node.js
- **MongoDB**: NoSQL database for storing blog posts
- **Mongoose**: ODM for MongoDB
- **EJS**: Templating engine for server-side rendering
- **Semantic UI**: CSS framework for styling
- **Body-parser**: Middleware for parsing request bodies
- **Method-override**: Middleware for supporting PUT and DELETE methods
- **Express-sanitizer**: Middleware for sanitizing user input

## Getting Started

### Prerequisites

- Node.js (v14 or higher)
- MongoDB (running locally on port 27017)
- npm or yarn

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd blog-site-restful-routing
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start MongoDB (if not already running):

   ```bash
   mongod
   ```

4. Start the application:

   ```bash
   node app.js
   ```

5. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

```
├── app.js                 # Main application file with routes and server setup
├── package.json           # Dependencies and scripts
├── public/
│   └── stylesheets/
│       └── app.css        # Custom styles
└── views/
    ├── index.ejs          # Homepage displaying all blog posts
    ├── new.ejs            # Form for creating new posts
    ├── show.ejs           # Individual blog post view
    ├── edit.ejs           # Form for editing posts
    └── partials/
        ├── header.ejs     # Navigation header
        └── footer.ejs     # Footer
```

## RESTful Routes

| Method | Route           | Description            |
| ------ | --------------- | ---------------------- |
| GET    | /               | Redirect to /blogs     |
| GET    | /blogs          | Display all blog posts |
| GET    | /blogs/new      | Show new post form     |
| POST   | /blogs          | Create new blog post   |
| GET    | /blogs/:id      | Show specific post     |
| GET    | /blogs/:id/edit | Show edit form         |
| PUT    | /blogs/:id      | Update specific post   |
| DELETE | /blogs/:id      | Delete specific post   |

## Database Schema

Each blog post contains:

- **title**: String - The blog post title
- **image**: String - URL to the blog post image
- **body**: String - The main content of the blog post
- **created**: Date - Automatically set to current date when created

## Usage

1. **View Posts**: Visit the homepage to see all blog posts
2. **Create Post**: Click "New Post" to add a new blog entry
3. **Read Post**: Click on any post title to view the full content
4. **Edit Post**: Click "Edit" on a post to modify it
5. **Delete Post**: Click "Delete" to remove a post

## Security Features

- **Input Sanitization**: All user input is sanitized to prevent XSS attacks
- **Method Override**: Supports PUT and DELETE methods for RESTful operations

## Styling

The application uses Semantic UI for a clean, professional look with:

- Fixed navigation bar
- Card-based layout for blog posts
- Responsive design for mobile devices
- Custom CSS for additional styling

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.</content>
<parameter name="filePath">/Users/ankitdabas/Learn/Web-Dev-Demo-Projects/Express/Blog_Site(RESTful Routing)/README.md
