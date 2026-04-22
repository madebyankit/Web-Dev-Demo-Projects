/**
 * REACT STATE CHEAT SHEET — ARRAYS & OBJECTS (IMMUTABLE PATTERNS)
 *
 * Rule: NEVER mutate state directly.
 * Always return a NEW array/object using spread, map, filter, etc.
 *
 * Mental model:
 * - filter → remove
 * - map → update
 * - spread (...) → copy
 */

import { useState } from "react";

/* =========================
   🟦 INITIAL STATE SETUP
========================= */

const [items, setItems] = useState([
  { id: 1, name: "Item 1", price: 10 },
  { id: 2, name: "Item 2", price: 20 },
]);

const [user, setUser] = useState({
  name: "John Doe",
  age: 24,
  address: {
    city: "Sample City",
    zip: "000000",
  },
});

/* =========================
   🔁 ARRAY OPERATIONS
========================= */

/* ➕ ADD ONE ITEM */
setItems(prev => {
  // Implicit return: spread operator creates new array with added item
  return [
    ...prev,
    { id: 3, name: "Item 3", price: 30 },
  ];
});

/* ➕➕ ADD MULTIPLE ITEMS */
setItems(prev => {
  // Implicit return: spread prev array and spread multiple new items into one array
  return [
    ...prev,
    ...[
      { id: 4, name: "Item 4", price: 40 },
      { id: 5, name: "Item 5", price: 50 },
    ],
  ];
});

/* ❌ REMOVE ITEM (by id) */
setItems(prev => {
  // Implicit return: filter returns new array excluding items with id === 2
  return prev.filter(item => item.id !== 2);
});

/* ❌ REMOVE MULTIPLE ITEMS */
const idsToRemove = [1, 3];
setItems(prev => {
  // Implicit return: filter removes items whose IDs are in the idsToRemove array
  return prev.filter(item => !idsToRemove.includes(item.id));
});

/* 🔁 UPDATE ONE ITEM */
setItems(prev => {
  // Implicit return: map over array, spread matching item with new price, return others unchanged
  return prev.map(item =>
    item.id === 2
      ? { ...item, price: 99 }
      : item
  );
});

/* 🔁 UPDATE MULTIPLE ITEMS (condition-based) */
setItems(prev => {
  // Implicit return: map over array and increase price by 10 for items with price < 30
  return prev.map(item =>
    item.price < 30
      ? { ...item, price: item.price + 10 }
      : item
  );
});

/* 🔄 REPLACE ENTIRE ARRAY */
// Implicit return: directly set new array, completely replacing the old state
setItems([
  { id: 100, name: "New Item", price: 999 },
]);

/* 🧹 CLEAR ARRAY */
// Implicit return: set empty array, removing all items
setItems([]);

/* 🔀 TOGGLE VALUE INSIDE ARRAY */
setItems(prev => {
  // Implicit return: map over array and toggle the active boolean for item with id === 1
  return prev.map(item =>
    item.id === 1
      ? { ...item, active: !item.active }
      : item
  );
});

/* 🔍 FIND INDEX + UPDATE (rare but useful) */
setItems(prev => {
  // Find the index of item with id === 2
  const index = prev.findIndex(i => i.id === 2);
  // If item not found, return previous state unchanged
  if (index === -1) return prev;

  // Create new array by spreading (avoid mutation)
  const updated = [...prev];
  // Update the item at the found index with new price
  updated[index] = { ...updated[index], price: 999 };
  // Return the updated array
  return updated;
});

/* 📦 INSERT AT SPECIFIC POSITION */
setItems(prev => {
  // Create new item to insert
  const newItem = { id: 6, name: "Inserted", price: 60 };
  // Return new array: items before index 1, the new item, and items from index 1 onwards
  return [
    ...prev.slice(0, 1),
    newItem,
    ...prev.slice(1),
  ];
});

/* 🔃 SORT ARRAY */
setItems(prev => {
  // Implicit return: spread into new array (to avoid mutation) and sort by price ascending
  return [...prev].sort((a, b) => a.price - b.price);
});

/* 🔄 REVERSE ARRAY */
setItems(prev => {
  // Implicit return: spread into new array (to avoid mutation) and reverse the order
  return [...prev].reverse();
});

/* =========================
   🟩 OBJECT OPERATIONS
========================= */

/* ✏️ UPDATE SINGLE FIELD */
setUser(prev => {
  // Implicit return: spread user object and override the name field
  return {
    ...prev,
    name: "New Name",
  };
});

/* ✏️ UPDATE MULTIPLE FIELDS */
setUser(prev => {
  // Implicit return: spread user object and override multiple fields (name and age)
  return {
    ...prev,
    name: "Ankit Sharma",
    age: 25,
  };
});

/* 🧠 UPDATE NESTED OBJECT */
setUser(prev => {
  // Implicit return: spread user, spread nested address object, and override city field
  return {
    ...prev,
    address: {
      ...prev.address,
      city: "Mumbai",
    },
  };
});

/* ❌ REMOVE FIELD FROM OBJECT */
setUser(prev => {
  // Destructure to extract age field and keep all other properties in rest
  const { age, ...rest } = prev;
  // Implicit return: return object without the age property
  return rest;
});

/* 🔁 TOGGLE BOOLEAN */
setUser(prev => {
  // Implicit return: spread user object and toggle the isActive boolean field
  return {
    ...prev,
    isActive: !prev.isActive,
  };
});

/* =========================
   ⚠️ COMMON MISTAKES (DON’T DO THIS)
========================= */

// ❌ Direct mutation
items.push({ id: 10 }); // WRONG

// ❌ Direct update
items[0].price = 999; // WRONG

// ❌ Mutating object
user.name = "Hacked"; // WRONG

/* =========================
   🧠 PRO TIP (IMPORTANT)
========================= */

/*
 * Always use functional updates when new state depends on old state:
 *
 * setState(prev => ...)
 *
 * This avoids stale state bugs (very common in async updates).
 */