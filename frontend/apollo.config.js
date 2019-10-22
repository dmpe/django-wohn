const path = require('path')

// Load .env files
const { loadEnv } = require('vue-cli-plugin-apollo/utils/load-env')
const env = loadEnv([
  path.resolve(__dirname, '.env'),
  path.resolve(__dirname, '.env.local')
])

// server and client properties for apollo CLI
// https://www.apollographql.com/docs/references/apollo-config/
module.exports = {
  client: {
    service: {
      name: 'melive-online',
      url: 'https://www.melive.xyz/graphql'
    },
    includes: ['src/**/*.{js,jsx,ts,tsx,vue,gql}']
  },
  service: {
    endpoint: {
      url: 'https://www.melive.xyz/graphql'
    }
  }
}
