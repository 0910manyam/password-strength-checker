import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true,
    host: true // Allow network access for mobile testing
  },
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    // Ensure service worker and manifest are copied
    rollupOptions: {
      input: {
        main: './index.html'
      }
    }
  },
  publicDir: 'public' // Ensure public files are served
})
