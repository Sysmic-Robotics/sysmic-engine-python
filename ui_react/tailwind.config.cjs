/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'electric-blue': '#014ba0',
        'robots': '#48A3A7',
        'robots-hover': '#93C2C4', 
      }
    },
  },
  plugins: [],
}
