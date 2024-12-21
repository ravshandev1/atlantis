
tailwind.config = {
  content: ["/css/font.css"],
  theme: {
    screens:{
      xs: '480px',
      sm:'640px',
      md:'768px',
      lg:'1024px',
      xl:'1280px',
    },
    container: {
      padding: {
        DEFAULT: '20px',
        sm: '0.9rem',
        lg: '1rem',
        xl: '1.2rem'
      },
      center: 'true',
    },
    fontFamily: {
      cambria: "Cambria",
    },
    extend: {

      lineClamp: {
        8: '8',
      },
      colors: {
        icon:"#F8F7F3",
        green: "#15594D",
        border: "#447A71",
        currentGray: "#363636",
      },
    },
  },
};
