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
      lintGQL: true
    }
  },
  configureWebpack: {
    plugins: [
      new CompressionPlugin({
        cache: true,
      })
    ]
  },
  chainWebpack: config => {
    // GraphQL Loader
    config.module
      .rule('graphql')
      .test(/\.graphql$/)
      .use('graphql-tag/loader')
        .loader('graphql-tag/loader')
        .end()
  }
};
