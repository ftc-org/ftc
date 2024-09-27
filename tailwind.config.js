/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: [
      './**/templates/*.html',
  ],
  theme: {
    extend: {
      colors: {
          'aljazeera-red': '#d21a1c',
      }
  }
  },
  plugins: [],
}
