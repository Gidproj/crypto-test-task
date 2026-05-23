/** @type {import('next').NextConfig} */
const nextConfig = {
  eslint: {
    // Эта строчка отключает проверку ESLint при сборке на Vercel
    ignoreDuringBuilds: true,
  },
};

export default nextConfig;