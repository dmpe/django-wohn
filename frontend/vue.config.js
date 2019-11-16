const CompressionPlugin = require("compression-webpack-plugin");

module.exports = {
  productionSourceMap: false,
  runtimeCompiler: true,
  devServer: {
    host: "0.0.0.0",
    allowedHosts: ["melive.xyz", "frontend.melive.xyz", "backend", "localhost"]
  },
  pluginOptions: {
    apollo: {
      lintGQL: false
    }
  },
  configureWebpack: {
    plugins: [
      new CompressionPlugin({
        cache: true,
      })
    ]
  }
};
