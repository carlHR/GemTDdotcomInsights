# How to use

Copy the following code below, open the browser inspector on `gemtowerdefense.com`, go to Console, paste it there, and press enter to confirm. Enjoy!

```
function VBox(classes='') {
   let vbox = document.createElement('div');
   vbox.className += ' vbox ' + classes;
   return vbox;
}
function VBoxContent() {
   let args = [...arguments];
   let b = VBox();
   for (let arg of args) {
      b.appendChild(arg);
   }
   return b;
}
function HBox(classes='') {
   let hbox = document.createElement('div');
   hbox.className += ' hbox ' + classes;
   return hbox;
}
function HBoxContent() {
   let args = [...arguments];
   let b = HBox();
   for (let arg of args) {
      b.appendChild(arg);
   }
   return b;
}
function Stretch(classes='') {
   let s = document.createElement('div');
   s.className += ' strech ' + classes;
   return s;
}
function Space1(classes='') {
   let s = document.createElement('div');
   s.className += ' space1 ' + classes;
   return s;
}
function Space2(classes='') {
   let s = document.createElement('div');
   s.className += ' space2 ' + classes;
   return s;
}
function Space4(classes='') {
   let s = document.createElement('div');
   s.className += ' space4 ' + classes;
   return s;
}
function Space8(classes='') {
   let s = document.createElement('div');
   s.className += ' space8 ' + classes;
   return s;
}
function Space16(classes='') {
   let s = document.createElement('div');
   s.className += ' space16 ' + classes;
   return s;
}
function Space32(classes='') {
   let s = document.createElement('div');
   s.className += ' space32 ' + classes;
   return s;
}
function Space64(classes='') {
   let s = document.createElement('div');
   s.className += ' space64 ' + classes;
   return s;
}
function TextBlock(text, align='left') {
   let d = HBox('div');
   let b = VBoxContent(Stretch(), d, Stretch());
   switch (align) {
   case 'center':
      d.appendChild(Stretch());
      d.appendChild(document.createTextNode(text));
      d.appendChild(Stretch());
      break;
   case 'left':
      d.appendChild(document.createTextNode(text));
      d.appendChild(Stretch());
      break;
   case 'right':
      d.appendChild(Stretch());
      d.appendChild(document.createTextNode(text));
      break;
   default:
      d.appendChild(document.createTextNode(text));
      break;
   }
   d.clear = function() {
      while (d.lastChild != null) {
         d.removeChild(d.lastChild);
      }
   };
   d.push = function(a) {
      d.appendChild(a);
   }
   d.setText = function(t) {
      d.clear();
      d.push(t);
   }
   b.clear = d.clear;
   b.push = d.push;
   b.setText = d.setText;
   return b;
}
function Title(t) {
   let tt = TextBlock(t, 'left');
   tt.className += ' title';
   return tt;
}

// Source: https://angel-rs.github.io/css-color-filter-generator/
// Expand shorthand form (e.g. "03F") to full form (e.g. "0033FF")
function expandHex(hextexp) {
   const shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
   hextexp = hextexp.replace(shorthandRegex, (m, r, g, b) => {
   return r + r + g + g + b + b;
   });
   return hextexp;
}

function rgbToHex(r, g, b) {
   function componentToHex(c) {
   var hex = c.toString(16);
   return hex.length == 1 ? "0" + hex : hex;
   }

   return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}

function hexToRgb(hex) {
   const expandedHex = expandHex(hex);
   const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(expandedHex);
   return result
   ? [
      parseInt(result[1], 16),
      parseInt(result[2], 16),
      parseInt(result[3], 16),
      ]
   : null;
}

function trimRgb(rgb) {
   const [r, g, b] = rgb
   .replace(/rgb\(|\) /i, "")
   .split(",")
   .map((x) => parseInt(x));
   return [r, g, b];
}

class Color {
   constructor(r, g, b) {
   this.set(r, g, b);
   }

   toRgb() {
   return `rgb(${Math.round(this.r)}, ${Math.round(this.g)}, ${Math.round(
      this.b
   )})`;
   }

   toHex() {
   return rgbToHex(Math.round(this.r), Math.round(this.g), Math.round(this.b));
   }

   set(r, g, b) {
   this.r = this.clamp(r);
   this.g = this.clamp(g);
   this.b = this.clamp(b);
   }

   hueRotate(angle = 0) {
   angle = (angle / 180) * Math.PI;
   const sin = Math.sin(angle);
   const cos = Math.cos(angle);

   this.multiply([
      0.213 + cos * 0.787 - sin * 0.213,
      0.715 - cos * 0.715 - sin * 0.715,
      0.072 - cos * 0.072 + sin * 0.928,
      0.213 - cos * 0.213 + sin * 0.143,
      0.715 + cos * 0.285 + sin * 0.14,
      0.072 - cos * 0.072 - sin * 0.283,
      0.213 - cos * 0.213 - sin * 0.787,
      0.715 - cos * 0.715 + sin * 0.715,
      0.072 + cos * 0.928 + sin * 0.072,
   ]);
   }

   grayscale(value = 1) {
   this.multiply([
      0.2126 + 0.7874 * (1 - value),
      0.7152 - 0.7152 * (1 - value),
      0.0722 - 0.0722 * (1 - value),
      0.2126 - 0.2126 * (1 - value),
      0.7152 + 0.2848 * (1 - value),
      0.0722 - 0.0722 * (1 - value),
      0.2126 - 0.2126 * (1 - value),
      0.7152 - 0.7152 * (1 - value),
      0.0722 + 0.9278 * (1 - value),
   ]);
   }

   sepia(value = 1) {
   this.multiply([
      0.393 + 0.607 * (1 - value),
      0.769 - 0.769 * (1 - value),
      0.189 - 0.189 * (1 - value),
      0.349 - 0.349 * (1 - value),
      0.686 + 0.314 * (1 - value),
      0.168 - 0.168 * (1 - value),
      0.272 - 0.272 * (1 - value),
      0.534 - 0.534 * (1 - value),
      0.131 + 0.869 * (1 - value),
   ]);
   }

   saturate(value = 1) {
   this.multiply([
      0.213 + 0.787 * value,
      0.715 - 0.715 * value,
      0.072 - 0.072 * value,
      0.213 - 0.213 * value,
      0.715 + 0.285 * value,
      0.072 - 0.072 * value,
      0.213 - 0.213 * value,
      0.715 - 0.715 * value,
      0.072 + 0.928 * value,
   ]);
   }

   multiply(matrix) {
   const newR = this.clamp(
      this.r * matrix[0] + this.g * matrix[1] + this.b * matrix[2]
   );
   const newG = this.clamp(
      this.r * matrix[3] + this.g * matrix[4] + this.b * matrix[5]
   );
   const newB = this.clamp(
      this.r * matrix[6] + this.g * matrix[7] + this.b * matrix[8]
   );
   this.r = newR;
   this.g = newG;
   this.b = newB;
   }

   brightness(value = 1) {
   this.linear(value);
   }
   contrast(value = 1) {
   this.linear(value, -(0.5 * value) + 0.5);
   }

   linear(slope = 1, intercept = 0) {
   this.r = this.clamp(this.r * slope + intercept * 255);
   this.g = this.clamp(this.g * slope + intercept * 255);
   this.b = this.clamp(this.b * slope + intercept * 255);
   }

   invert(value = 1) {
   this.r = this.clamp((value + (this.r / 255) * (1 - 2 * value)) * 255);
   this.g = this.clamp((value + (this.g / 255) * (1 - 2 * value)) * 255);
   this.b = this.clamp((value + (this.b / 255) * (1 - 2 * value)) * 255);
   }

   hsl() {
   // Code taken from https://stackoverflow.com/a/9493060/2688027, licensed under CC BY-SA.
   const r = this.r / 255;
   const g = this.g / 255;
   const b = this.b / 255;
   const max = Math.max(r, g, b);
   const min = Math.min(r, g, b);
   let h,
      s,
      l = (max + min) / 2;

   if (max === min) {
      h = s = 0;
   } else {
      const d = max - min;
      s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
      switch (max) {
      case r:
         h = (g - b) / d + (g < b ? 6 : 0);
         break;

      case g:
         h = (b - r) / d + 2;
         break;

      case b:
         h = (r - g) / d + 4;
         break;
      }
      h /= 6;
   }

   return {
      h: h * 100,
      s: s * 100,
      l: l * 100,
   };
   }

   clamp(value) {
   if (value > 255) {
      value = 255;
   } else if (value < 0) {
      value = 0;
   }
   return value;
   }
}

class Solver {
   constructor(target, baseColor) {
   this.target = target;
   this.targetHSL = target.hsl();
   this.reusedColor = new Color(0, 0, 0);
   }

   solve() {
   const result = this.solveNarrow(this.solveWide());
   return {
      values: result.values,
      loss: result.loss,
      filter: this.css(result.values),
      filterRaw: this.raw(result.values),
   };
   }

   solveWide() {
   const A = 5;
   const c = 15;
   const a = [60, 180, 18000, 600, 1.2, 1.2];

   let best = { loss: Infinity };
   for (let i = 0; best.loss > 25 && i < 3; i++) {
      const initial = [50, 20, 3750, 50, 100, 100];
      const result = this.spsa(A, a, c, initial, 1000);
      if (result.loss < best.loss) {
      best = result;
      }
   }
   return best;
   }

   solveNarrow(wide) {
   const A = wide.loss;
   const c = 2;
   const A1 = A + 1;
   const a = [0.25 * A1, 0.25 * A1, A1, 0.25 * A1, 0.2 * A1, 0.2 * A1];
   return this.spsa(A, a, c, wide.values, 500);
   }

   spsa(A, a, c, values, iters) {
   const alpha = 1;
   const gamma = 0.16666666666666666;

   let best = null;
   let bestLoss = Infinity;
   const deltas = new Array(6);
   const highArgs = new Array(6);
   const lowArgs = new Array(6);

   for (let k = 0; k < iters; k++) {
      const ck = c / Math.pow(k + 1, gamma);
      for (let i = 0; i < 6; i++) {
      deltas[i] = Math.random() > 0.5 ? 1 : -1;
      highArgs[i] = values[i] + ck * deltas[i];
      lowArgs[i] = values[i] - ck * deltas[i];
      }

      const lossDiff = this.loss(highArgs) - this.loss(lowArgs);
      for (let i = 0; i < 6; i++) {
      const g = (lossDiff / (2 * ck)) * deltas[i];
      const ak = a[i] / Math.pow(A + k + 1, alpha);
      values[i] = fix(values[i] - ak * g, i);
      }

      const loss = this.loss(values);
      if (loss < bestLoss) {
      best = values.slice(0);
      bestLoss = loss;
      }
   }
   return { values: best, loss: bestLoss };

   function fix(value, idx) {
      let max = 100;
      if (idx === 2 /* saturate */) {
      max = 7500;
      } else if (idx === 4 /* brightness */ || idx === 5 /* contrast */) {
      max = 200;
      }

      if (idx === 3 /* hue-rotate */) {
      if (value > max) {
         value %= max;
      } else if (value < 0) {
         value = max + (value % max);
      }
      } else if (value < 0) {
      value = 0;
      } else if (value > max) {
      value = max;
      }
      return value;
   }
   }

   loss(filters) {
   // Argument is array of percentages.
   const color = this.reusedColor;
   color.set(0, 0, 0);

   color.invert(filters[0] / 100);
   color.sepia(filters[1] / 100);
   color.saturate(filters[2] / 100);
   color.hueRotate(filters[3] * 3.6);
   color.brightness(filters[4] / 100);
   color.contrast(filters[5] / 100);

   const colorHSL = color.hsl();
   return (
      Math.abs(color.r - this.target.r) +
      Math.abs(color.g - this.target.g) +
      Math.abs(color.b - this.target.b) +
      Math.abs(colorHSL.h - this.targetHSL.h) +
      Math.abs(colorHSL.s - this.targetHSL.s) +
      Math.abs(colorHSL.l - this.targetHSL.l)
   );
   }

   raw(filters) {
   function fmt(idx, multiplier = 1) {
      return Math.round(filters[idx] * multiplier);
   }
   return `brightness(0) saturate(100%) invert(${fmt(0)}%) sepia(${fmt(
      1
   )}%) saturate(${fmt(2)}%) hue-rotate(${fmt(3, 3.6)}deg) brightness(${fmt(
      4
   )}%) contrast(${fmt(5)}%)`;
   }

   css(filters) {
   function fmt(idx, multiplier = 1) {
      return Math.round(filters[idx] * multiplier);
   }
   return `filter: brightness(0) saturate(100%) invert(${fmt(0)}%) sepia(${fmt(
      1
   )}%) saturate(${fmt(2)}%) hue-rotate(${fmt(3, 3.6)}deg) brightness(${fmt(
      4
   )}%) contrast(${fmt(5)}%);`;
   }
}

// Receives rgb color, returns the corresponding filter as string.
function AngleRSColors(red, green, blue) {
   const color = new Color(red, green, blue);
   const solver = new Solver(color);
   let result = solver.solve();
   let tries = 0;

   while (result.loss > 5 && tries < 200) {
      result = solver.solve();
      ++tries;
   }

   if (result.loss > 5) {
      console.warn('AngleRSColors has attempted its best to get the best aprox color. But it failed. Loss score: ' + String(result.loss));
   }

   return result.filterRaw;
}

function CustomUI() {
   let canvas = document.getElementsByTagName('canvas')[0];
   let inner = document.createElement('div');
   let outer = document.createElement('div');
   let image = document.createElement('img');
   let style = document.createElement('style');
   let menu = VBox('menu expand');

   let imageColorFilter = '';
   let imageOpacity = 1.0;
   let useColorFilterState = true;

   function applyImageFilter() {
      if (useColorFilterState) {
         image.setAttribute('style', 'filter: ' + imageColorFilter + '; opacity: ' + imageOpacity + ';');
      } else {
         image.setAttribute('style', 'opacity: ' + imageOpacity + ';');
      }
   }

   // Image Overlay Source:
   // https://stackoverflow.com/a/14843923/14956120
   style.innerHTML = `
.outer{ 
   width:705px; height:504px; 
}
.inner{ 
   width:100%; height:100%; 
   position:relative;
}
.cover{ 
   width:100%; height:100%; 
   position:absolute; top:0px; left:0px;
}
.image{
   pointer-events: none; top: 20px;
   min-width: 520px; min-height: 520px;
   max-width: 520px; max-height: 520px;
}
.menu{
   margin: 8px;
   border: 1px solid silver;
   border-radius: 4px;
   padding: 8px;
}
.expand {
   width: 100%;
}
.menu .title {
   font-size: medium;
}
.vbox{
   display: flex;
   flex-direction: column;
}
.hbox{
   display: flex;
   flex-direction: row;
}
.strech{
   flex: 1;
}
.space1 {
   min-width: 1px;
   max-width: 1px;
   min-height: 1px;
   max-height: 1px;
}
.space2 {
   min-width: 2px;
   max-width: 2px;
   min-height: 2px;
   max-height: 2px;
}
.space4 {
   min-width: 4px;
   max-width: 4px;
   min-height: 4px;
   max-height: 4px;
}
.space8 {
   min-width: 8px;
   max-width: 8px;
   min-height: 8px;
   max-height: 8px;
}
.space16 {
   min-width: 16px;
   max-width: 16px;
   min-height: 16px;
   max-height: 16px;
}
.space32 {
   min-width: 32px;
   max-width: 32px;
   min-height: 32px;
   max-height: 32px;
}
.space64 {
   min-width: 64px;
   max-width: 64px;
   min-height: 64px;
   max-height: 64px;
}
`;
   
   // apply default grid.
   
   inner.className = 'inner';
   outer.className = 'outer';
   image.className = 'cover image';
   canvas.className += ' cover';

   document.head.appendChild(style);

   let fileChooser = document.createElement('input');
   let toggleButton = document.createElement('input');
   let opacitySlider = document.createElement('input');
   let colorPicker = document.createElement('input');
   let opacityOutput = TextBlock('(100%)');
   let useColorFilter = document.createElement('input');
   let restoreTemplate = document.createElement('input');

   function restoreImageTemplate() {
      fileChooser.value = null;
      image.src = 'data:image/png;base64,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';
      colorPicker.value = '#808080';
      opacitySlider.value = 0.5;
      imageColorFilter = AngleRSColors(128, 128, 128);
      imageOpacity = 0.5;
      opacitySlider.value = 0.5;
      opacityOutput.setText(document.createTextNode('(' + String(Math.floor(opacitySlider.value * 10000) / 100) + '%)'));
      useColorFilter.checked = true;
      useColorFilterState = true;
      applyImageFilter();
   }

   toggleButton.type = 'checkbox';
   toggleButton.value = 'Show Grid';
   toggleButton.checked = true;
   opacitySlider.type = 'range';
   opacitySlider.min = 0;
   opacitySlider.max = 1;
   opacitySlider.value = 1;
   opacitySlider.step = 'any';
   colorPicker.type = 'color';
   colorPicker.value = '#808080';
   useColorFilter.type = 'checkbox';
   useColorFilter.checked = true;
   restoreTemplate.type = 'button';
   restoreTemplate.value = 'Reset Template';

   restoreImageTemplate();

   // Reading files content from html, if necessary
   // https://stackoverflow.com/a/64113219/14956120
   fileChooser.type = 'file';
   fileChooser.onchange = async function (event) {
      const file = event.target.files.item(0);
      let text = await file.bytes();
      image.src = 'data:image/png;base64,' + text.toBase64();
      applyImageFilter();
   };

   toggleButton.onchange = function (event) {
      if (toggleButton.checked) {
         image.style.display = 'block';
      } else {
         image.style.display = 'none';
      }
   }

   colorPicker.addEventListener('input', function (e) {
      let rgb = hexToRgb(e.target.value);
      imageColorFilter = AngleRSColors(rgb[0], rgb[1], rgb[2]);
      applyImageFilter();
   });

   opacitySlider.addEventListener('input', function (e) {
      opacityOutput.setText(document.createTextNode('(' + String(Math.floor(e.target.value * 10000) / 100) + '%)'));
      imageOpacity = e.target.value;
      applyImageFilter();
   });

   useColorFilter.onchange = function (event) {
      useColorFilterState = useColorFilter.checked;
      applyImageFilter();
   }

   restoreTemplate.onclick = function (event) {
      restoreImageTemplate();
   }

   let hbox;
   let vbox;
   let submenu;

   hbox = HBox();
   canvas.parentNode.parentNode.appendChild(Space8());
   canvas.parentNode.parentNode.appendChild(hbox);

   hbox.appendChild(Stretch());
   hbox.appendChild(menu);
   hbox.appendChild(Stretch());

   menu.appendChild(Title('Map Template:'))
   submenu = VBox('menu');
   submenu.appendChild(HBoxContent(TextBlock(' - template: '), Space4(), fileChooser, Stretch()));
   submenu.appendChild(Space4());
   submenu.appendChild(HBoxContent(TextBlock(' - color: '), Space4(), colorPicker, Stretch()));
   submenu.appendChild(Space4());
   submenu.appendChild(HBoxContent(TextBlock(' - apply css filter: '), useColorFilter, Stretch()));
   submenu.appendChild(Space4());
   submenu.appendChild(HBoxContent(TextBlock(' - opacity: '), Space4(), opacitySlider, Space4(), opacityOutput, Stretch()));
   submenu.appendChild(Space4());
   submenu.appendChild(HBoxContent(TextBlock(' - visibility: '), Space4(), toggleButton, Stretch()));
   submenu.appendChild(Space4());
   submenu.appendChild(HBoxContent(restoreTemplate, Stretch()));
   submenu.appendChild(Space4());
   menu.appendChild(submenu);
   menu.appendChild(Space8());

   canvas.parentNode.appendChild(outer);
   canvas.parentNode.removeChild(canvas);

   outer.setAttribute('style', 'min-width: 705px; min-height: 540px;');

   outer.appendChild(inner);
   inner.appendChild(canvas);
   inner.appendChild(image);
}

CustomUI();

```
