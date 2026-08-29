# CanvasCart

> **Where Art Meets Elegance.**

CanvasCart is a full-stack art marketplace built with Django, designed to provide a premium e-commerce experience for discovering, exploring, and purchasing original artwork.

The project combines a luxury-inspired frontend with a Django backend, database-driven artwork management, authentication, cart and wishlist functionality, order management, and Razorpay payment integration.

---

## Overview

CanvasCart is designed around a simple idea:

**Buying art should feel like discovering art.**

Instead of treating artwork like ordinary e-commerce products, CanvasCart focuses on presentation, curated collections, artist information, and a clean luxury-inspired interface.

Users can browse artwork without creating an account, explore individual artwork details, and authenticate only when they want to interact with the marketplace.

---

## Features

### Authentication

- User signup and login
- Session-based authentication
- Password hashing using Django's password hashing utilities
- Email validation
- Password strength validation
- Logout and session termination
- Dynamic navigation based on authentication state

### Gallery

- Database-driven artwork gallery
- Artwork categories
- Artwork images
- Artist information
- Pricing
- Individual artwork detail pages
- Related artwork section
- Category filtering

### Shopping Cart

- Add artwork to cart
- Increase quantity
- Decrease quantity
- Remove artwork
- Dynamic quantity-based pricing
- Total item calculation
- Total cart price
- Checkout redirection

### Wishlist

- Add artwork to wishlist
- Remove artwork from wishlist
- Dedicated wishlist page
- Wishlist items stored per user
- Wishlist functionality protected behind authentication

### Orders

- Buy Now functionality
- Cart-based checkout
- Order creation
- Order items
- Quantity and price tracking
- Delivery information
- Order total calculation

### Payment

- Razorpay payment integration
- Razorpay checkout
- Payment status tracking
- Payment flow connected to orders

### Admin

CanvasCart uses Django's built-in admin panel for managing backend data such as:

- Users
- Artwork
- Orders
- Order items
- Cart items
- Wishlist items

---

## User Flow

### Guest User

```text
Home
  ↓
Gallery
  ↓
Artwork Details
  ↓
Login / Signup