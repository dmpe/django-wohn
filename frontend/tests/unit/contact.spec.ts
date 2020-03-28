import "jest";
import Contact from "@/views/Contact.vue";
import { shallowMount, mount } from "@vue/test-utils";

describe("Contact.vue", () => {
  const contactWrapper = mount(Contact);

  it("Contact view contains a contact form", () => {
    // Contains works around selectors
    expect(contactWrapper.contains("#form-contact")).toBe(true);
  });
});
