import Vue, { VNode } from "vue";

declare global {
  namespace JSX {
    // Tslint:disable no-empty-interface
    type Element = VNode;
    // Tslint:disable no-empty-interface
    type ElementClass = Vue;
    interface IntrinsicElements {
      [elem: string]: any;
    }
  }
}
