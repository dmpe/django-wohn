import gql from "graphql-tag";

export const returnLastFive = gql`query {
  homeProperties{
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
