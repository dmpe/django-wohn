module.exports = {
  env: {
    browser: true,
    es6: true
  },
  parser: "vue-eslint-parser",
  extends: [
    "eslint:recommended",
    "plugin:vue/recommended",
    "plugin:@typescript-eslint/eslint-recommended",
    "plugin:@typescript-eslint/recommended"
  ],
  parserOptions: {
    parser: "@typescript-eslint/parser",
    project: "tsconfig.json",
    ecmaVersion: 2017,
    sourceType: "module",
    ecmaFeatures: {
      "jsx": true
    }
  },
  plugins: ["@typescript-eslint", "@typescript-eslint/tslint"],
  rules: {
    "@typescript-eslint/adjacent-overload-signatures": "warn",
    "@typescript-eslint/array-type": "warn",
    "@typescript-eslint/ban-types": "warn",
    "@typescript-eslint/class-name-casing": "warn",
    "@typescript-eslint/consistent-type-assertions": "warn",
    "@typescript-eslint/consistent-type-definitions": "warn",
    "@typescript-eslint/explicit-member-accessibility": [
      "warn",
      {
        accessibility: "explicit"
      }
    ],
    "@typescript-eslint/indent": [
      "warn",
      2,
      {
        ObjectExpression: "first",
        FunctionDeclaration: {
          parameters: "first"
        },
        FunctionExpression: {
          parameters: "first"
        }
      }
    ],
    "@typescript-eslint/interface-name-prefix": "off",
    "@typescript-eslint/member-delimiter-style": [
      "error",
      {
        multiline: {
          delimiter: "semi",
          requireLast: true
        },
        singleline: {
          delimiter: "semi",
          requireLast: false
        }
      }
    ],
    "@typescript-eslint/member-ordering": "warn",
    "@typescript-eslint/no-empty-function": "warn",
    "@typescript-eslint/no-empty-interface": "warn",
    "@typescript-eslint/no-explicit-any": "off",
    "@typescript-eslint/no-misused-new": "warn",
    "@typescript-eslint/no-namespace": "warn",
    "@typescript-eslint/no-parameter-properties": "off",
    "@typescript-eslint/no-this-alias": "warn",
    "@typescript-eslint/no-use-before-declare": "off",
    "@typescript-eslint/no-var-requires": "warn",
    "@typescript-eslint/prefer-for-of": "warn",
    "@typescript-eslint/prefer-function-type": "warn",
    "@typescript-eslint/prefer-namespace-keyword": "warn",
    "@typescript-eslint/quotes": ["warn", "double"],
    "@typescript-eslint/semi": ["warn", "always"],
    "@typescript-eslint/space-within-parens": ["warn", "always"],
    "@typescript-eslint/triple-slash-reference": "warn",
    "@typescript-eslint/type-annotation-spacing": "warn",
    "@typescript-eslint/unified-signatures": "warn",
    "arrow-body-style": "warn",
    "arrow-parens": ["warn", "as-needed"],
    camelcase: "warn",
    "capitalized-comments": "warn",
    complexity: "off",
    "constructor-super": "warn",
    curly: "warn",
    "dot-notation": "warn",
    "eol-last": "warn",
    eqeqeq: ["warn", "smart"],
    "guard-for-in": "warn",
    "id-blacklist": [
      "warn",
      "any",
      "Number",
      "number",
      "String",
      "string",
      "Boolean",
      "boolean",
      "Undefined",
      "undefined"
    ],
    "id-match": "warn",
    "import/no-extraneous-dependencies": "warn",
    "import/no-internal-modules": "warn",
    "import/order": "warn",
    "max-classes-per-file": ["warn", 1],
    "max-len": [
      "warn",
      {
        code: 120
      }
    ],
    "new-parens": "warn",
    "no-bitwise": "warn",
    "no-caller": "warn",
    "no-cond-assign": "warn",
    "no-console": "warn",
    "no-debugger": "warn",
    "no-duplicate-case": "warn",
    "no-duplicate-imports": "warn",
    "no-empty": "warn",
    "no-eval": "warn",
    "no-extra-bind": "warn",
    "no-fallthrough": "off",
    "no-invalid-this": "off",
    "no-multiple-empty-lines": "off",
    "no-new-func": "warn",
    "no-new-wrappers": "warn",
    "no-redeclare": "warn",
    "no-return-await": "warn",
    "no-sequences": "warn",
    "no-shadow": [
      "warn",
      {
        hoist: "all"
      }
    ],
    "no-sparse-arrays": "warn",
    "no-template-curly-in-string": "warn",
    "no-throw-literal": "warn",
    "no-trailing-spaces": "warn",
    "no-undef-init": "warn",
    "no-underscore-dangle": "warn",
    "no-unsafe-finally": "warn",
    "no-unused-expressions": "warn",
    "no-unused-labels": "warn",
    "no-var": "warn",
    "object-shorthand": "warn",
    "one-var": ["warn", "never"],
    "prefer-arrow/prefer-arrow-functions": "warn",
    "prefer-const": "warn",
    "prefer-object-spread": "warn",
    "quote-props": ["warn", "consistent-as-needed"],
    radix: "warn",
    "space-before-function-paren": [
      "warn",
      {
        anonymous: "never",
        asyncArrow: "always",
        named: "never"
      }
    ],
    "spaced-comment": "warn",
    "use-isnan": "warn",
    "valid-typeof": "off",
    "@typescript-eslint/tslint/config": [
      "error",
      {
        rules: {
          "import-spacing": true,
          "jsdoc-format": [true, "check-multiline-start"],
          "no-reference-import": true,
          "one-line": [
            true,
            "check-catch",
            "check-else",
            "check-finally",
            "check-open-brace",
            "check-whitespace"
          ],
          "prefer-conditional-expression": true,
          "trailing-comma": [
            true,
            {
              singleline: "never",
              multiline: "always",
              esSpecCompliant: true
            }
          ],
          whitespace: [
            true,
            "check-branch",
            "check-decl",
            "check-operator",
            "check-separator",
            "check-type",
            "check-typecast",
            "check-type-operator",
            "check-rest-spread"
          ]
        }
      }
    ]
  }
};
