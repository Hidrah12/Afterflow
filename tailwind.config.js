/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../src/apps/core/templates/**/*.html",
  ],
  theme: {
    extend: {},
    screens: {
      '2xl': {'max': '1535px'},
      // => @media (max-width: 1535px) { ... }

      'xl': {'max': '1279px'},
      // => @media (max-width: 1279px) { ... }

      'bxl': {'max': '1170px'},

      'lg': {'max': '1023px'},
      // => @media (max-width: 1023px) { ... }

      'blg': {'max': '910px'},

      'md': {'max': '767px'},
      // => @media (max-width: 767px) { ... }

      'sm': {'max': '639px'},
      // => @media (max-width: 639px) { ... }
      
      'bsm': {'max': '580px'},
      'xr': {'max': '420px'},
      'se': {'max': '375px'},
      'mn': {'min': '767px'},
      'blgMin': {'min': '910px'},
    },
  },
  darkMode:'class',
  plugins: [],
}
