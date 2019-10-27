module.exports = {
  productionSourceMap: false,
  runtimeCompiler: true,
  devServer: {
    host: "0.0.0.0",
    allowedHosts: ["melive.xyz", "frontend.melive.xyz", "backend", "localhost"]
  }
};
