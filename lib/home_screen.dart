import 'package:flutter/material.dart';
import 'signup_screen.dart';
import 'login_screen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white, // Sets the clean white background
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 30.0),
        child: Column(
          mainAxisAlignment:
              MainAxisAlignment.center, // Centers everything vertically
          children: [
            // 1. App Logo - Displays the brand image from your assets folder
            Image.asset(
              'assets/dirkmhob_logo.png',
              width: 250,
              errorBuilder: (context, error, stackTrace) {
                return const Text(
                  'DirkMhob',
                  style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold),
                );
              },
            ),
            const SizedBox(height: 40),

            // 2. Welcome Greeting
            const Text(
              'Welcome!',
              style: TextStyle(
                fontSize: 32,
                fontWeight: FontWeight.w400,
                color: Colors.black87,
              ),
            ),
            const SizedBox(height: 60),

            // 3. Main Login Button (Email/Username)
            SizedBox(
              width: double.infinity, // Makes button take full width
              height: 50,
              child: ElevatedButton(
                onPressed: () {
                  // Connect to the new login layout structure
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => const LoginScreen(),
                    ),
                  );
                },
                style: ElevatedButton.styleFrom(
                  backgroundColor: const Color(0xFF007BFF), // Branding Blue
                  shape: const RoundedRectangleBorder(
                    borderRadius: BorderRadius.zero, // Sharp square edges
                  ),
                ),
                child: const Text(
                  'Log in',
                  style: TextStyle(color: Colors.white, fontSize: 18),
                ),
              ),
            ),
            const SizedBox(height: 15),

            // 4. Guest Access - Allows users to browse before signing up
            SizedBox(
              width: double.infinity,
              height: 50,
              child: OutlinedButton(
                onPressed: () {
                  // TODO: Navigate to Main Map/Discovery screen
                },
                style: OutlinedButton.styleFrom(
                  side: const BorderSide(color: Colors.black54),
                  shape: const RoundedRectangleBorder(
                    borderRadius: BorderRadius.zero,
                  ),
                ),
                child: const Text(
                  'Continue as Guest',
                  style: TextStyle(color: Colors.black87),
                ),
              ),
            ),
            const SizedBox(height: 25),

            // 5. Footer - Link for new users to create an account
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text("Don't have an account? "),
                GestureDetector(
                  onTap: () {
                    // Enact screen navigation target shift
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => const SignUpScreen(),
                      ),
                    );
                  },
                  child: const Text(
                    "Signup",
                    style: TextStyle(
                      color: Color(0xFF007BFF),
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
