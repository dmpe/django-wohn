import 'jest';
import Home from "@/views/Home.vue";
import { shallowMount, mount } from "@vue/test-utils";

describe("Home.vue", () => {
  const homeWrapper = mount(Home);

  it("Home view containers Header", () => {
    expect(homeWrapper.html()).toContain("navbarLoginForm");
  });
});

