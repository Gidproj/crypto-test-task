/** @type {import('next').NextConfig} */
const nextConfig = {
  eslint: {
    // Внимание: это отключает проверку ESLint при сборке на Vercel
    ignoreDuringBuilds: true,
  },
};

export default nextConfig;