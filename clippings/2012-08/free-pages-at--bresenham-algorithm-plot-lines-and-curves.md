---
url: "http://free.pages.at/easyfilter/bresenham.html"
captured_at: "2012-08-09T10:23:52-03:00"
title: "Bresenham Algorithm - plot lines and curves"
domain: "free-pages-at"
---

## The Beauty of Bresenham's Algorithm

A simple implementation to plot lines, circles, ellipses and Bézier curves.

### [The Algorithm](http://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm)

This page introduces a compact and efficient implementation of Bresenham's algorithm to plot lines, circles, ellipses and Bézier curves.

A detailed documentation of the algorithm and more program examples are availble in PDF: [Bresenham.pdf](http://free.pages.at/easyfilter/bresenham.pdf).

Four C-program examples of the document are listed below.

The source code of the samples is also available: [bresenham.c](http://free.pages.at/easyfilter/bresenham.c)

|  |  |
| --- | --- |
| [Line](http://en.wikipedia.org/wiki/Line_drawing_algorithm) A simple example of Bresenham's line algorithm.   ``` void plotLine(int x0, int y0, int x1, int y1) {   int dx =  abs(x1-x0), sx = x0<x1 ? 1 : -1;   int dy = -abs(y1-y0), sy = y0<y1 ? 1 : -1;    int err = dx+dy, e2; /* error value e_xy */     for(;;){  /* loop */     setPixel(x0,y0);     if (x0==x1 && y0==y1) break;     e2 = 2*err;     if (e2 >= dy) { err += dy; x0 += sx; } /* e_xy+e_x > 0 */     if (e2 <= dx) { err += dx; y0 += sy; } /* e_xy+e_y < 0 */   } } ``` | cedbaf267889333c5c0eb30dc85bc9ce.png |
| [Circle](http://en.wikipedia.org/wiki/Midpoint_circle_algorithm) This is an implementation of the circle algorithm.   ``` void plotCircle(int xm, int ym, int r) {    int x = -r, y = 0, err = 2-2*r; /* II. Quadrant */     do {       setPixel(xm-x, ym+y); /*   I. Quadrant */       setPixel(xm-y, ym-x); /*  II. Quadrant */       setPixel(xm+x, ym-y); /* III. Quadrant */       setPixel(xm+y, ym+x); /*  IV. Quadrant */       r = err;       if (r <= y) err += ++y*2+1;           /* e_xy+e_y < 0 */       if (r > x || err > y) err += ++x*2+1; /* e_xy+e_x > 0 or no 2nd y-step */    } while (x < 0); } ``` | aaeb5c4cc8d97da339d1cc0d4f0d5deb.png |
| [Ellipse](http://en.wikipedia.org/wiki/Ellipse) This program example plots an ellipse inside a specified rectangle.   ``` void plotEllipseRect(int x0, int y0, int x1, int y1) {    int a = abs(x1-x0), b = abs(y1-y0), b1 = b&1; /* values of diameter */    long dx = 4*(1-a)*b*b, dy = 4*(b1+1)*a*a; /* error increment */    long err = dx+dy+b1*a*a, e2; /* error of 1.step */     if (x0 > x1) { x0 = x1; x1 += a; } /* if called with swapped points */    if (y0 > y1) y0 = y1; /* .. exchange them */    y0 += (b+1)/2; y1 = y0-b1;   /* starting pixel */    a *= 8*a; b1 = 8*b*b;     do {        setPixel(x1, y0); /*   I. Quadrant */        setPixel(x0, y0); /*  II. Quadrant */        setPixel(x0, y1); /* III. Quadrant */        setPixel(x1, y1); /*  IV. Quadrant */        e2 = 2*err;        if (e2 <= dy) { y0++; y1--; err += dy += a; }  /* y step */         if (e2 >= dx || 2*err > dy) { x0++; x1--; err += dx += b1; } /* x step */    } while (x0 <= x1);        while (y0-y1 < b) {  /* too early stop of flat ellipses a=1 */        setPixel(x0-1, y0); /* -> finish tip of ellipse */        setPixel(x1+1, y0++);         setPixel(x0-1, y1);        setPixel(x1+1, y1--);     } } ``` | e54333c0b1bfffac12bb03af07b3392a.png |
| [Bézier curve](http://en.wikipedia.org/wiki/B%C3%A9zier_curve) This program example plots a quadratic Bézier curve limited to gradients without sign change. | |
| ``` void plotBasicBezier(int x0, int y0, int x1, int y1, int x2, int y2) {                               int sx = x2-x1, sy = y2-y1;   long xx = x0-x1, yy = y0-y1, xy;         /* relative values for checks */   double dx, dy, err, cur = xx*sy-yy*sx;                    /* curvature */    assert(xx*sx <= 0 && yy*sy <= 0);  /* sign of gradient must not change */    if (sx*(long)sx+sy*(long)sy > xx*xx+yy*yy) { /* begin with longer part */      x2 = x0; x0 = sx+x1; y2 = y0; y0 = sy+y1; cur = -cur;  /* swap P0 P2 */   }     if (cur != 0) {                                    /* no straight line */     xx += sx; xx *= sx = x0 < x2 ? 1 : -1;           /* x step direction */     yy += sy; yy *= sy = y0 < y2 ? 1 : -1;           /* y step direction */     xy = 2*xx*yy; xx *= xx; yy *= yy;          /* differences 2nd degree */     if (cur*sx*sy < 0) {                           /* negated curvature? */       xx = -xx; yy = -yy; xy = -xy; cur = -cur;     }     dx = 4.0*sy*cur*(x1-x0)+xx-xy;             /* differences 1st degree */     dy = 4.0*sx*cur*(y0-y1)+yy-xy;     xx += xx; yy += yy; err = dx+dy+xy;                /* error 1st step */         do {                                     setPixel(x0,y0);                                     /* plot curve */       if (x0 == x2 && y0 == y2) return;  /* last pixel -> curve finished */       y1 = 2*err < dx;                  /* save value for test of y step */       if (2*err > dy) { x0 += sx; dx -= xy; err += dy += yy; } /* x step */       if (    y1    ) { y0 += sy; dy -= xy; err += dx += xx; } /* y step */     } while (dy < 0 && dx > 0);   /* gradient negates -> algorithm fails */   }   plotLine(x0,y0, x2,y2);                  /* plot remaining part to end */ } ``` | 2de7c3c7b4a573358d0edf8897f1ee01.png |

#### Features of the rasterising algorithm:

- Universal: This algorithm plots lines, circles, ellipses, Bézier curves, etc.
- Fast: Draws complex curves nearly as fast as lines.
- Simple: Short and compact implementation.
- Exact: No approximation of the curve.

The principle of the algorithm could be used to rasterize any curve.
