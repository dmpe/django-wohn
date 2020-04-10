const CompressionPlugin = require("compression-webpack-plugin");
const PnpWebpackPlugin = require(`pnp-webpack-plugin`);

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
      PnpWebpackPlugin,
      new CompressionPlugin({
        cache: true,
      })
    ],
    resolveLoader: {
      plugins: [
        PnpWebpackPlugin.moduleLoader(module),
      ],
    },
  },
  // ChainWebpack: config => {
  //   // GraphQL Loader
  //   Config.module
  //     .rule('graphql')
  //     .test(/\.(graphql|gql)$/)
  //     .use('graphql-tag/loader')
  //     .loader('graphql-tag/loader')
  //     .end()
  // }
};
