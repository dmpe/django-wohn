import gql from "graphql-tag";

export const contactUs = gql`mutation($choices: String!, $email: String!, $name: String!, $subject: String!, $text: String!) {
  sendContactMsg(
    email: $email,
    name: $name,
    choices: $choices,
    subject: $subject,
    text: $text,
  ) {
    id,
    name,
    email,
    choices,
    subject,
    text
  }
}`;
