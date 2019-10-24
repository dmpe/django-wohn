module.exports = {
  productionSourceMap: false,
  runtimeCompiler: true,
  devServer: {
    allowedHosts: [
      'melive.xyz',
      'frontend.melive.xyz',
      'backend',
      'localhost'
    ]
  }
}
