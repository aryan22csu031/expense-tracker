const express = require('express');
const router = express.Router();

// Mock user data
const users = [
    { email: 'test@example.com', password: '123' }
];

// Login route
router.post('/login', (req, res) => {
    const { email, password } = req.body;

    const user = users.find(u => u.email === email && u.password === password);

    if (user) {
        res.status(200).json({ message: 'Login successful' });
    } else {
        res.status(401).json({ message: 'Invalid email or password' });
    }
});

module.exports = router;
