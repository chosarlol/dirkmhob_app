import 'package:flutter/material.dart';
import 'splash_screen.dart'; // This connects your splash screen

void main() {
  runApp(const DirkMhobApp());
}

class DirkMhobApp extends StatelessWidget {
  const DirkMhobApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: SplashScreen(), // This starts the app on your logo screen
    );
  }
}
