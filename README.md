<!--

@license Apache-2.0

Copyright (c) 2022 The Stdlib Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

-->


<details>
  <summary>
    About stdlib...
  </summary>
  <p>We believe in a future in which the web is a preferred environment for numerical computation. To help realize this future, we've built stdlib. stdlib is a standard library, with an emphasis on numerical and scientific computation, written in JavaScript (and C) for execution in browsers and in Node.js.</p>
  <p>The library is fully decomposable, being architected in such a way that you can swap out and mix and match APIs and functionality to cater to your exact preferences and use cases.</p>
  <p>When you use stdlib, you can be absolutely certain that you are using the most thorough, rigorous, well-written, studied, documented, tested, measured, and high-quality code out there.</p>
  <p>To join us in bringing numerical computing to the web, get started by checking us out on <a href="https://github.com/stdlib-js/stdlib">GitHub</a>, and please consider <a href="https://opencollective.com/stdlib">financially supporting stdlib</a>. We greatly appreciate your continued support!</p>
</details>

# gammasgn

[![NPM version][npm-image]][npm-url] [![Build Status][test-image]][test-url] [![Coverage Status][coverage-image]][coverage-url] <!-- [![dependencies][dependencies-image]][dependencies-url] -->

> Sign of the [gamma function][@stdlib/math/base/special/gamma].

<section class="intro">

The sign of the [gamma-function][@stdlib/math/base/special/gamma] is defined as

<!-- <equation class="equation" label="eq:gamma_sign_function" align="center" raw="\operatorname{gammasgn} ( x ) = \begin{cases} 1 & \textrm{if}\ \Gamma > 0 \\ -1 & \textrm{if}\ \Gamma < 0 \\ 0 & \textrm{otherwise}\ \end{cases}" alt="Sign of the gamma function"> -->

```math
\mathop{\mathrm{gammasgn}} ( x ) = \begin{cases} 1 & \textrm{if}\ \Gamma > 0 \\ -1 & \textrm{if}\ \Gamma < 0 \\ 0 & \textrm{otherwise}\ \end{cases}
```

<!-- </equation> -->

The [gamma function][@stdlib/math/base/special/gamma] can be computed as the product of `gammasgn(x)` and `exp(gammaln(x))`.

</section>

<!-- /.intro -->



<section class="usage">

## Usage

To use in Observable,

```javascript
gammasgn = require( 'https://cdn.jsdelivr.net/gh/stdlib-js/math-base-special-gammasgn@umd/browser.js' )
```

To vendor stdlib functionality and avoid installing dependency trees for Node.js, you can use the UMD server build:

```javascript
var gammasgn = require( 'path/to/vendor/umd/math-base-special-gammasgn/index.js' )
```

To include the bundle in a webpage,

```html
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/stdlib-js/math-base-special-gammasgn@umd/browser.js"></script>
```

If no recognized module system is present, access bundle contents via the global scope:

```html
<script type="text/javascript">
(function () {
    window.gammasgn;
})();
</script>
```

#### gammasgn( x )

Returns the sign of the [gamma function][@stdlib/math/base/special/gamma].

```javascript
var v = gammasgn( 1.0 );
// returns 1.0

v = gammasgn( -2.5 );
// returns -1.0

v = gammasgn( 0.0 );
// returns 0.0

v = gammasgn( NaN );
// returns NaN
```

</section>

<!-- /.usage -->

<section class="notes">

## Notes

-   The [gamma function][@stdlib/math/base/special/gamma] is not defined for negative integer values (i.e., `gamma(x) === NaN` when `x` is a negative integer). The [natural logarithm of the gamma function][@stdlib/math/base/special/gammaln] is defined for negative integer values (i.e., `gammaln(x) === Infinity` when `x` is a negative integer). Accordingly, in order for the equality `gamma(x) === gammasgn(x) * exp(gammaln(x))` to hold (i.e., return `NaN`), `gammasgn` needs to either return `NaN` or `0`. By convention, this function returns `0`.

</section>

<!-- /. notes -->

<section class="examples">

## Examples

<!-- eslint no-undef: "error" -->

```html
<!DOCTYPE html>
<html lang="en">
<body>
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/stdlib-js/random-array-uniform@umd/browser.js"></script>
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/stdlib-js/console-log-each-map@umd/browser.js"></script>
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/stdlib-js/math-base-special-gammasgn@umd/browser.js"></script>
<script type="text/javascript">
(function () {

var opts = {
    'dtype': 'float64'
};
var x = uniform( 100, -10.0, 10.0, opts );

logEachMap( 'x: %0.4f, f(x): %0.4f', x, gammasgn );

})();
</script>
</body>
</html>
```

</section>

<!-- /.examples -->

<!-- C interface documentation. -->



<!-- Section for related `stdlib` packages. Do not manually edit this section, as it is automatically populated. -->

<section class="related">

* * *

## See Also

-   <span class="package-name">[`@stdlib/math-base/special/gamma`][@stdlib/math/base/special/gamma]</span><span class="delimiter">: </span><span class="description">gamma function.</span>

</section>

<!-- /.related -->

<!-- Section for all links. Make sure to keep an empty line after the `section` element and another before the `/section` close. -->


<section class="main-repo" >

* * *

## Notice

This package is part of [stdlib][stdlib], a standard library for JavaScript and Node.js, with an emphasis on numerical and scientific computing. The library provides a collection of robust, high performance libraries for mathematics, statistics, streams, utilities, and more.

For more information on the project, filing bug reports and feature requests, and guidance on how to develop [stdlib][stdlib], see the main project [repository][stdlib].

#### Community

[![Chat][chat-image]][chat-url]

---

## License

See [LICENSE][stdlib-license].


## Copyright

Copyright &copy; 2016-2025. The Stdlib [Authors][stdlib-authors].

</section>

<!-- /.stdlib -->

<!-- Section for all links. Make sure to keep an empty line after the `section` element and another before the `/section` close. -->

<section class="links">

[npm-image]: http://img.shields.io/npm/v/@stdlib/math-base-special-gammasgn.svg
[npm-url]: https://npmjs.org/package/@stdlib/math-base-special-gammasgn

[test-image]: https://github.com/stdlib-js/math-base-special-gammasgn/actions/workflows/test.yml/badge.svg?branch=main
[test-url]: https://github.com/stdlib-js/math-base-special-gammasgn/actions/workflows/test.yml?query=branch:main

[coverage-image]: https://img.shields.io/codecov/c/github/stdlib-js/math-base-special-gammasgn/main.svg
[coverage-url]: https://codecov.io/github/stdlib-js/math-base-special-gammasgn?branch=main

<!--

[dependencies-image]: https://img.shields.io/david/stdlib-js/math-base-special-gammasgn.svg
[dependencies-url]: https://david-dm.org/stdlib-js/math-base-special-gammasgn/main

-->

[chat-image]: https://img.shields.io/gitter/room/stdlib-js/stdlib.svg
[chat-url]: https://app.gitter.im/#/room/#stdlib-js_stdlib:gitter.im

[stdlib]: https://github.com/stdlib-js/stdlib

[stdlib-authors]: https://github.com/stdlib-js/stdlib/graphs/contributors

[umd]: https://github.com/umdjs/umd
[es-module]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules

[deno-url]: https://github.com/stdlib-js/math-base-special-gammasgn/tree/deno
[deno-readme]: https://github.com/stdlib-js/math-base-special-gammasgn/blob/deno/README.md
[umd-url]: https://github.com/stdlib-js/math-base-special-gammasgn/tree/umd
[umd-readme]: https://github.com/stdlib-js/math-base-special-gammasgn/blob/umd/README.md
[esm-url]: https://github.com/stdlib-js/math-base-special-gammasgn/tree/esm
[esm-readme]: https://github.com/stdlib-js/math-base-special-gammasgn/blob/esm/README.md
[branches-url]: https://github.com/stdlib-js/math-base-special-gammasgn/blob/main/branches.md

[stdlib-license]: https://raw.githubusercontent.com/stdlib-js/math-base-special-gammasgn/main/LICENSE

[@stdlib/math/base/special/gamma]: https://github.com/stdlib-js/math-base-special-gamma/tree/umd

[@stdlib/math/base/special/gammaln]: https://github.com/stdlib-js/math-base-special-gammaln/tree/umd

<!-- <related-links> -->

<!-- </related-links> -->

</section>

<!-- /.links -->
