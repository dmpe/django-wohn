import "jest";
import NotFound from "@/views/NotFound.vue";
import { shallowMount, mount } from "@vue/test-utils";

describe("NotFound/404.vue", () => {
  const notFoundWrapper = mount(NotFound);

  it("NotFound/404 can be displayed", () => {
    expect(notFoundWrapper.html()).toContain("picsum");
  });
});
