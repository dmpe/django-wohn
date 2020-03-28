import gql from "graphql-tag";

// Rename query here because vue either needs to update name
// Be renamed here
// See https://github.com/vuejs/vue-apollo/issues/700#issuecomment-511418849
export const myProperties = gql`query {
  myProperties:
    meliveUser(id:2) {
      id,
      homeProperties {
        id
      }
    }
}`;
