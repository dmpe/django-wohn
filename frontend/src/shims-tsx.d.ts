import Vue, { VNode } from "vue";

declare global {
  namespace JSX {
    // Tslint:disable no-empty-interface
    interface Element extends VNode {}
    // Tslint:disable no-empty-interface
    interface ElementClass extends Vue {}
    interface IntrinsicElements {
      [elem: string]: any;
    }
  }
}
