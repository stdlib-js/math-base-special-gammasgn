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

# gammasgn

[![NPM version][npm-image]][npm-url] [![Build Status][test-image]][test-url] [![Coverage Status][coverage-image]][coverage-url] <!-- [![dependencies][dependencies-image]][dependencies-url] -->

> Sign of the [gamma function][@stdlib/math/base/special/gamma].

<section class="intro">

The sign of the [gamma-function][@stdlib/math/base/special/gamma] is defined as

<!-- <equation class="equation" label="eq:gamma_sign_function" align="center" raw="\operatorname{gammasgn} ( x ) = \begin{cases} 1 & \textrm{if}\ \Gamma > 1 \\ -1 & \textrm{if}\ \Gamma < 1 \\ 0 & \textrm{otherwise}\ \end{cases}" alt="Sign of the gamma function"> -->

<div class="equation" align="center" data-raw-text="\operatorname{gammasgn} ( x ) = \begin{cases} 1 &amp; \textrm{if}\ \Gamma &gt; 1 \\ -1 &amp; \textrm{if}\ \Gamma &lt; 1 \\ 0 &amp; \textrm{otherwise}\ \end{cases}" data-equation="eq:gamma_sign_function">
    <img src="https://cdn.jsdelivr.net/gh/stdlib-js/stdlib@50b141156b147529227e2eb4247eda81c781dec9/lib/node_modules/@stdlib/math/base/special/gammasgn/docs/img/equation_gamma_sign_function.svg" alt="Sign of the gamma function">
    <br>
</div>

<!-- </equation> -->

The [gamma function][@stdlib/math/base/special/gamma] can be computed as the product of `gammasgn(x)` and `exp(gammaln(x))`.

</section>

<!-- /.intro -->



<section class="usage">

## Usage

```javascript
import gammasgn from 'https://cdn.jsdelivr.net/gh/stdlib-js/math-base-special-gammasgn@deno/mod.js';
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

-    The [gamma function][@stdlib/math/base/special/gamma] is not defined for negative integer values (i.e., `gamma(x) === NaN` when `x` is a negative integer). The [natural logarithm of the gamma function][@stdlib/math/base/special/gammaln] is defined for negative integer values (i.e., `gammaln(x) === Infinity` when `x` is a negative integer). Accordingly, in order for the equality `gamma(x) === gammasgn(x) * exp(gammaln(x))` to hold (i.e., return `NaN`), `gammasgn` needs to either return `NaN` or `0`. By convention, this function returns `0`.

</section>

<!-- /. notes -->

<section class="examples">

## Examples

<!-- eslint no-undef: "error" -->

```javascript
import linspace from 'https://cdn.jsdelivr.net/gh/stdlib-js/array-base-linspace@deno/mod.js';
import gammasgn from 'https://cdn.jsdelivr.net/gh/stdlib-js/math-base-special-gammasgn@deno/mod.js';

var x = linspace( -10.0, 10.0, 100 );

var i;
for ( i = 0; i < x.length; i++ ) {
    console.log( 'x: %d, f(x): %d', x[ i ], gammasgn( x[ i ] ) );
}
```

</section>

<!-- /.examples -->

<!-- Section for related `stdlib` packages. Do not manually edit this section, as it is automatically populated. -->

<section class="related">

</section>

<!-- /.related -->

<!-- Section for all links. Make sure to keep an empty line after the `section` element and another before the `/section` close. -->


<section class="main-repo" >

* * *

## Notice

This package is part of [stdlib][stdlib], a standard library with an emphasis on numerical and scientific computing. The library provides a collection of robust, high performance libraries for mathematics, statistics, streams, utilities, and more.

For more information on the project, filing bug reports and feature requests, and guidance on how to develop [stdlib][stdlib], see the main project [repository][stdlib].

#### Community

[![Chat][chat-image]][chat-url]

---

## License

See [LICENSE][stdlib-license].


## Copyright

Copyright &copy; 2016-2023. The Stdlib [Authors][stdlib-authors].

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
[chat-url]: https://gitter.im/stdlib-js/stdlib/

[stdlib]: https://github.com/stdlib-js/stdlib

[stdlib-authors]: https://github.com/stdlib-js/stdlib/graphs/contributors

[umd]: https://github.com/umdjs/umd
[es-module]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules

[deno-url]: https://github.com/stdlib-js/math-base-special-gammasgn/tree/deno
[umd-url]: https://github.com/stdlib-js/math-base-special-gammasgn/tree/umd
[esm-url]: https://github.com/stdlib-js/math-base-special-gammasgn/tree/esm
[branches-url]: https://github.com/stdlib-js/math-base-special-gammasgn/blob/main/branches.md

[stdlib-license]: https://raw.githubusercontent.com/stdlib-js/math-base-special-gammasgn/main/LICENSE

[@stdlib/math/base/special/gamma]: https://github.com/stdlib-js/math-base-special-gamma/tree/deno

[@stdlib/math/base/special/gammaln]: https://github.com/stdlib-js/math-base-special-gammaln/tree/deno

<!-- <related-links> -->

<!-- </related-links> -->

</section>

<!-- /.links -->
