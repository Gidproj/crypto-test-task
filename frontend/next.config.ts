/** @type {import('next').NextConfig} */
const nextConfig = {
  // Добавьте этот блок:
  eslint: {
    ignoreDuringBuilds: true,
  },
};

export default nextConfig;