import gql from "graphql-tag";

// rename query here because vue either needs to update name
// be renamed here
// see https://github.com/vuejs/vue-apollo/issues/700#issuecomment-511418849 */
export const returnLastFive = gql`query {
  returnLastFive: homeProperties {
    id,
    propertyCreated,
    propertyOfferedBy {
      id
    },
    propertyRooms,
    propertySizeInSqMeters,
    propertySizeInSqFoot,
    propertyPriceInEur,
    propertyPriceInCzk,
    propertyPriceInUsd,
    propertyGarage,
    propertyStatus,
    propertyFurnished,
    propertyWashMachine,
    propertyAddressStreet,
    propertyAddressCityTown,
    propertyAddressZipcode,
    houseGardenSizeInSqMeters,
  }
}`;
