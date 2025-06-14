# This file is part of project py-tailwind-utils
#
# Copyright (c) [2023] by Monallabs.in.
# This file is released under the MIT License.
#
# Author(s): Kabira K. (webworks.monallabs.in).
# MIT License
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys

current_module = sys.modules[__name__]

from .style_tags import noop
from . import style_values as sv
from .style_tags import outline as outlineTag, boxshadow as boxShadowTag


class _DisplayBox:
    _sv_class = sv.DisplayBox

    @property
    def b(cls):
        return noop / cls._sv_class.b

    @property
    def bi(cls):
        return noop / cls._sv_class.bi

    @property
    def i(cls):
        return noop / cls._sv_class.i

    @property
    def f(cls):
        return noop / cls._sv_class.f

    @property
    def fi(cls):
        return noop / cls._sv_class.fi

    @property
    def t(cls):
        return noop / cls._sv_class.t

    @property
    def it(cls):
        return noop / cls._sv_class.it

    @property
    def tcaption(cls):
        return noop / cls._sv_class.tcaption

    @property
    def tcell(cls):
        return noop / cls._sv_class.tcell

    @property
    def tc(cls):
        return noop / cls._sv_class.tc

    @property
    def tcg(cls):
        return noop / cls._sv_class.tcg

    @property
    def thg(cls):
        return noop / cls._sv_class.thg

    @property
    def tfg(cls):
        return noop / cls._sv_class.tfg

    @property
    def thg(cls):
        return noop / cls._sv_class.thg    

    @property
    def trg(cls):
        return noop / cls._sv_class.trg

    @property
    def tr(cls):
        return noop / cls._sv_class.tr

    @property
    def flowroot(cls):
        return noop / cls._sv_class.flowroot

    @property
    def g(cls):
        return noop / cls._sv_class.g

    @property
    def ig(cls):
        return noop / cls._sv_class.ig

    @property
    def contents(cls):
        return noop / cls._sv_class.contents

    @property
    def li(cls):
        return noop / cls._sv_class.li

    @property
    def h(cls):
        return noop / cls._sv_class.h
    
    
# class _DisplayBox:
#     _sv_class = sv.DisplayBox

#     @property
#     def b(cls):
#         return noop / sv.DisplayBox.b

#     @property
#     def bi(cls):
#         return noop / sv.DisplayBox.bi

#     @property
#     def i(cls):
#         return noop / sv.DisplayBox.i

#     @property
#     def f(cls):
#         return noop / sv.DisplayBox.f

#     @property
#     def fi(cls):
#         return noop / sv.DisplayBox.fi

#     @property
#     def t(cls):
#         return noop / sv.DisplayBox.t

#     @property
#     def g(cls):
#         return noop / sv.DisplayBox.g


DisplayBox = _DisplayBox()


# class _BoxLayout:
#     _sv_class = sv.BoxLayout

#     @property
#     def b(cls):
#         return noop / sv.BoxLayout.b

#     @property
#     def bi(cls):
#         return noop / sv.BoxLayout.bi

#     @property
#     def i(cls):
#         return noop / sv.BoxLayout.i

#     @property
#     def f(cls):
#         return noop / sv.BoxLayout.f

#     @property
#     def fi(cls):
#         return noop / sv.BoxLayout.fi

#     @property
#     def t(cls):
#         return noop / sv.BoxLayout.t

#     @property
#     def g(cls):
#         return noop / sv.BoxLayout.g


# BoxLayout = _BoxLayout()


class _WrapAround:
    _sv_class = sv.WrapAround

    
    @property
    def s(cls):
        return noop / sv.WrapAround.s

    
    @property
    def e(cls):
        return noop / sv.WrapAround.e

    
    @property
    def r(cls):
        return noop / sv.WrapAround.r

    @property
    def l(cls):
        return noop / sv.WrapAround.l

    @property
    def n(cls):
        return noop / sv.WrapAround.n


WrapAround = _WrapAround()


class _ClearWrap:
    _sv_class = sv.ClearWrap

    @property
    def l(cls):
        return noop / sv.ClearWrap.l

    @property
    def r(cls):
        return noop / sv.ClearWrap.r

    @property
    def b(cls):
        return noop / sv.ClearWrap.b

    @property
    def n(cls):
        return noop / sv.ClearWrap.n


ClearWrap = _ClearWrap()

        
class _ObjectFit:
    _sv_class = sv.ObjectFit

    @property
    def cn(cls):
        return noop / sv.ObjectFit.cn

    @property
    def cv(cls):
        return noop / sv.ObjectFit.cv

    @property
    def f(cls):
        return noop / sv.ObjectFit.f

    @property
    def n(cls):
        return noop / sv.ObjectFit.n

    @property
    def sd(cls):
        return noop / sv.ObjectFit.sd


ObjectFit = _ObjectFit()


class _ObjectPosition:
    _sv_class = sv.ObjectPosition

    @property
    def b(cls):
        return noop / sv.ObjectPosition.b

    @property
    def c(cls):
        return noop / sv.ObjectPosition.c

    @property
    def l(cls):
        return noop / sv.ObjectPosition.l

    @property
    def lb(cls):
        return noop / sv.ObjectPosition.lb

    @property
    def lt(cls):
        return noop / sv.ObjectPosition.lt

    @property
    def r(cls):
        return noop / sv.ObjectPosition.r

    @property
    def rb(cls):
        return noop / sv.ObjectPosition.rb

    @property
    def t(cls):
        return noop / sv.ObjectPosition.t


ObjectPosition = _ObjectPosition()


# class _Visibility:
#     _sv_class = sv.Visibility

#     @property
#     def v(cls):
#         return noop / sv.Visibility.v

#     @property
#     def nv(cls):
#         return noop / sv.Visibility.nv


# Visibility = _Visibility()

class _FlexDirection:
    _sv_class = sv.FlexDirection

    @property
    def row(cls):
        return noop / sv.FlexDirection.row

    @property
    def rrow(cls):
        return noop / sv.FlexDirection.rrow

    @property
    def col(cls):
        return noop / sv.FlexDirection.col

    @property
    def rcol(cls):
        return noop / sv.FlexDirection.rcol

FlexDirection = _FlexDirection()    

class _FlexWrap:
    _sv_class = sv.FlexWrap

    @property
    def w(cls):
        return noop / sv.FlexWrap.w

    @property
    def rw(cls):
        return noop / sv.FlexWrap.rw

    @property
    def nw(cls):
        return noop / sv.FlexWrap.nw

FlexWrap = _FlexWrap()

class _FlexResize:
    _sv_class = sv.FlexResize

    @property
    def one(cls):
        return noop / sv.FlexResize.one

    @property
    def auto(cls):
        return noop / sv.FlexResize.auto

    @property
    def initial(cls):
        return noop / sv.FlexResize.initial

    @property
    def none(cls):
        return noop / sv.FlexResize.none

    @property
    def grow(cls):
        return noop / sv.FlexResize.grow

    @property
    def nogrow(cls):
        return noop / sv.FlexResize.nogrow

    @property
    def shrink(cls):
        return noop / sv.FlexResize.shrink

    @property
    def noshrink(cls):
        return noop / sv.FlexResize.noshrink


FlexResize = _FlexResize()


class _JustifyContent:
    _sv_class = sv.JustifyContent

    @property
    def start(cls):
        return noop / sv.JustifyContent.start

    @property
    def end(cls):
        return noop / sv.JustifyContent.end

    @property
    def center(cls):
        return noop / sv.JustifyContent.center

    @property
    def between(cls):
        return noop / sv.JustifyContent.between

    @property
    def evenly(cls):
        return noop / sv.JustifyContent.evenly

    @property
    def around(cls):
        return noop / sv.JustifyContent.around


    @property
    def stretch(cls):
        return noop / sv.JustifyContent.stretch


    @property
    def normal(cls):
        return noop / sv.JustifyContent.normal
    

JustifyContent = _JustifyContent()


class _JustifyItems:
    _sv_class = sv.JustifyItems

    @property
    def start(cls):
        return noop / sv.JustifyItems.start

    @property
    def end(cls):
        return noop / sv.JustifyItems.end

    @property
    def center(cls):
        return noop / sv.JustifyItems.center

    @property
    def stretch(cls):
        return noop / sv.JustifyItems.stretch


JustifyItems = _JustifyItems()


class _JustifySelf:
    _sv_class = sv.JustifySelf

    @property
    def auto(cls):
        return noop / sv.JustifySelf.auto

    @property
    def start(cls):
        return noop / sv.JustifySelf.start

    @property
    def end(cls):
        return noop / sv.JustifySelf.end

    @property
    def center(cls):
        return noop / sv.JustifySelf.center

    @property
    def stretch(cls):
        return noop / sv.JustifySelf.stretch


JustifySelf = _JustifySelf()


class _AlignContent:
    _sv_class = sv.AlignContent

    @property
    def start(cls):
        return noop / sv.AlignContent.start

    @property
    def end(cls):
        return noop / sv.AlignContent.end

    @property
    def center(cls):
        return noop / sv.AlignContent.center

    @property
    def between(cls):
        return noop / sv.AlignContent.between

    @property
    def evenly(cls):
        return noop / sv.AlignContent.evenly

    @property
    def around(cls):
        return noop / sv.AlignContent.around

    @property
    def normal(cls):
        return noop/sv.AlignContent.normal
    
    @property
    def baseline(cls):
        return noop/sv.AlignContent.baseline

    @property
    def stretch(cls):
        return noop/sv.AlignContent.stretch

    
    

AlignContent = _AlignContent()


class _AlignItems:
    _sv_class = sv.AlignItems

    @property
    def start(cls):
        return noop / sv.AlignItems.start

    @property
    def end(cls):
        return noop / sv.AlignItems.end

    @property
    def center(cls):
        return noop / sv.AlignItems.center

    @property
    def stretch(cls):
        return noop / sv.AlignItems.stretch

    @property
    def baseline(cls):
        return noop / sv.AlignItems.baseline


AlignItems = _AlignItems()


class _PlaceContent:
    _sv_class = sv.PlaceContent

    @property
    def start(cls):
        return noop / sv.PlaceContent.start

    @property
    def end(cls):
        return noop / sv.PlaceContent.end

    @property
    def center(cls):
        return noop / sv.PlaceContent.center

    @property
    def between(cls):
        return noop / sv.PlaceContent.between

    @property
    def evenly(cls):
        return noop / sv.PlaceContent.evenly

    @property
    def around(cls):
        return noop / sv.PlaceContent.around

    @property
    def stretch(cls):
        return noop / sv.PlaceContent.stretch


PlaceContent = _PlaceContent()


class _PlaceItems:
    _sv_class = sv.PlaceItems

    @property
    def start(cls):
        return noop / sv.PlaceItems.start

    @property
    def end(cls):
        return noop / sv.PlaceItems.end

    @property
    def center(cls):
        return noop / sv.PlaceItems.center

    @property
    def stretch(cls):
        return noop / sv.PlaceItems.stretch


PlaceItems = _PlaceItems()


class _PlaceSelf:
    _sv_class = sv.PlaceSelf

    @property
    def auto(cls):
        return noop / sv.PlaceSelf.auto

    @property
    def start(cls):
        return noop / sv.PlaceSelf.start

    @property
    def end(cls):
        return noop / sv.PlaceSelf.end

    @property
    def center(cls):
        return noop / sv.PlaceSelf.center

    @property
    def stretch(cls):
        return noop / sv.PlaceSelf.stretch


PlaceSelf = _PlaceSelf()


class _FontFamily:
    _sv_class = sv.FontFamily

    @property
    def sans(cls):
        return noop / sv.FontFamily.sans

    @property
    def serif(cls):
        return noop / sv.FontFamily.serif

    @property
    def mono(cls):
        return noop / sv.FontFamily.mono


FontFamily = _FontFamily()


class _FontStyle:
    _sv_class = sv.FontStyle

    @property
    def i(cls):
        return noop / sv.FontStyle.i

    @property
    def ni(cls):
        return noop / sv.FontStyle.ni


FontStyle = _FontStyle()


class _FontSmoothing:
    _sv_class = sv.FontSmoothing

    @property
    def a(cls):
        return noop / sv.FontSmoothing.a

    @property
    def sa(cls):
        return noop / sv.FontSmoothing.sa


FontSmoothing = _FontSmoothing()


class _FontSize:
    _sv_class = sv.FontSize

    @property
    def xs(cls):
        return noop / sv.FontSize.xs

    @property
    def sm(cls):
        return noop / sv.FontSize.sm

    @property
    def _(cls):
        return noop / sv.FontSize._

    @property
    def lg(cls):
        return noop / sv.FontSize.lg

    @property
    def xl(cls):
        return noop / sv.FontSize.xl

    @property
    def xl2(cls):
        return noop / sv.FontSize.xl2

    @property
    def xl3(cls):
        return noop / sv.FontSize.xl3

    @property
    def xl4(cls):
        return noop / sv.FontSize.xl4

    @property
    def xl5(cls):
        return noop / sv.FontSize.xl5

    @property
    def xl6(cls):
        return noop / sv.FontSize.xl6


FontSize = _FontSize()


class _FontWeight:
    _sv_class = sv.FontWeight

    @property
    def thin(cls):
        return noop / sv.FontWeight.thin

    @property
    def extralight(cls):
        return noop / sv.FontWeight.extralight

    @property
    def light(cls):
        return noop / sv.FontWeight.light

    @property
    def normal(cls):
        return noop / sv.FontWeight.normal

    @property
    def medium(cls):
        return noop / sv.FontWeight.medium

    @property
    def bold(cls):
        return noop / sv.FontWeight.bold

    @property
    def extrabold(cls):
        return noop / sv.FontWeight.extrabold

    @property
    def black(cls):
        return noop / sv.FontWeight.black

    @property
    def semibold(cls):
        return noop / sv.FontWeight.semibold


FontWeight = _FontWeight()


class _LetterSpace:
    _sv_class = sv.LetterSpace

    @property
    def tighter(cls):
        return noop / sv.LetterSpace.tighter

    @property
    def tight(cls):
        return noop / sv.LetterSpace.tight

    @property
    def normal(cls):
        return noop / sv.LetterSpace.normal

    @property
    def wide(cls):
        return noop / sv.LetterSpace.wide

    @property
    def wider(cls):
        return noop / sv.LetterSpace.wider

    @property
    def widest(cls):
        return noop / sv.LetterSpace.widest


LetterSpace = _LetterSpace()


class _LineHeight:
    _sv_class = sv.LineHeight

    @property
    def none(cls):
        return noop / sv.LineHeight.none

    @property
    def tight(cls):
        return noop / sv.LineHeight.tight

    @property
    def snug(cls):
        return noop / sv.LineHeight.snug

    @property
    def normal(cls):
        return noop / sv.LineHeight.normal

    @property
    def relaxed(cls):
        return noop / sv.LineHeight.relaxed

    @property
    def loose(cls):
        return noop / sv.LineHeight.loose


LineHeight = _LineHeight()


class _ListStyleType:
    _sv_class = sv.ListStyleType

    @property
    def none(cls):
        return noop / sv.ListStyleType.none

    @property
    def disc(cls):
        return noop / sv.ListStyleType.disc

    @property
    def decimal(cls):
        return noop / sv.ListStyleType.decimal

ListStyleType = _ListStyleType()

    
class _ListStylePosition:
    _sv_class = sv.ListStylePosition
    
    @property
    def i(cls):
        return noop / sv.ListStylePosition.i

    @property
    def o(cls):
        return noop / sv.ListStylePosition.o


ListStylePosition = _ListStylePosition()



class _TextAlign:
    _sv_class = sv.TextAlign

    @property
    def left(cls):
        return noop / sv.TextAlign.left

    @property
    def center(cls):
        return noop / sv.TextAlign.center

    @property
    def right(cls):
        return noop / sv.TextAlign.right

    @property
    def justify(cls):
        return noop / sv.TextAlign.justify

    @property
    def start(cls):
        return noop / sv.TextAlign.start

    @property
    def end(cls):
        return noop / sv.TextAlign.end


TextAlign = _TextAlign()


class _TextTransform:
    _sv_class = sv.TextTransform

    @property
    def u(cls):
        return noop / sv.TextTransform.u

    @property
    def l(cls):
        return noop / sv.TextTransform.l

    @property
    def c(cls):
        return noop / sv.TextTransform.c

    @property
    def n(cls):
        return noop / sv.TextTransform.n


TextTransform = _TextTransform()

class _TextWrap:
    _sv_class = sv.TextWrap
    
    @property
    def wrap(cls):
        return noop/sv.TextWrap.wrap
    

    @property
    def nowrap(cls):
        return noop/sv.TextWrap.nowrap

    
    @property
    def balance(cls):
        return noop/sv.TextWrap.balance

    
    @property
    def pretty(cls):
        return noop/sv.TextWrap.pretty

TextWrap = _TextWrap()

class _TextDecoration:
    _sv_class = sv.TextDecoration

    @property
    def underline(cls):
        return noop/sv.TextDecoration.underline

    @property
    def overline(cls):
        return noop/sv.TextDecoration.overline

    @property
    def linethrough(cls):
        return noop/sv.TextDecoration.linethrough

    @property
    def nounderline(cls):
        return noop/sv.TextDecoration.nounderline

TextDecoration = _TextDecoration()    

class _TextOverflow:
    _sv_class = sv.TextOverflow

    @property
    def truncate(cls):
        return noop/sv.TextOverflow.truncate


    @property
    def ellipsis(cls):
        return noop/sv.TextOverflow.ellipsis


    @property
    def clip(cls):
        return noop/sv.TextOverflow.clip


TextOverflow = _TextOverflow()

        
    
class _DecorationStyle:
    _sv_class = sv.DecorationStyle

    @property
    def solid(cls):
        return noop / sv.DecorationStyle.solid

    @property
    def dashed(cls):
        return noop / sv.DecorationStyle.dashed

    @property
    def dotted(cls):
        return noop / sv.DecorationStyle.dotted

    @property
    def double(cls):
        return noop / sv.DecorationStyle.double

    @property
    def wavy(cls):
        return noop / sv.DecorationStyle.wavy



DecorationStyle = _DecorationStyle()



    
class _VerticalAlign:
    _sv_class = sv.VerticalAlign

    @property
    def baseline(cls):
        return noop / sv.VerticalAlign.baseline

    @property
    def texttop(cls):
        return noop / sv.VerticalAlign.texttop
    

    @property
    def textbottom(cls):
        return noop / sv.VerticalAlign.textbottom

    @property
    def alignsub(cls):
        return noop / sv.VerticalAlign.alignsub


    @property
    def alignsuper(cls):
        return noop / sv.VerticalAlign.alignsuper
        
    
    
    @property
    def top(cls):
        return noop / sv.VerticalAlign.top

    @property
    def middle(cls):
        return noop / sv.VerticalAlign.middle

    @property
    def bottom(cls):
        return noop / sv.VerticalAlign.bottom


VerticalAlign = _VerticalAlign()


class _BackgroundAttachment:
    _sv_class = sv.BackgroundAttachment

    @property
    def f(cls):
        return noop / sv.BackgroundAttachment.f

    @property
    def l(cls):
        return noop / sv.BackgroundAttachment.l

    @property
    def s(cls):
        return noop / sv.BackgroundAttachment.s


BackgroundAttachment = _BackgroundAttachment()


class _BorderRadius:
    _sv_class = sv.BorderRadius

    @property
    def sm(cls):
        return noop / sv.BorderRadius.sm

    @property
    def md(cls):
        return noop / sv.BorderRadius.md

    @property
    def lg(cls):
        return noop / sv.BorderRadius.lg

    @property
    def full(cls):
        return noop / sv.BorderRadius.full

    @property
    def none(cls):
        return noop / sv.BorderRadius.none

    @property
    def _(cls):
        return noop / sv.BorderRadius._

    @property
    def xl(cls):
        return noop / sv.BorderRadius.xl

    @property
    def xl2(cls):
        return noop / sv.BorderRadius.xl2

    @property
    def xl3(cls):
        return noop / sv.BorderRadius.xl3

    @property
    def container(cls):
        return noop / sv.BorderRadius.container

    @property
    def base(cls):
        return noop / sv.BorderRadius.base    
    
    

BorderRadius = _BorderRadius()


class _BorderStyle:
    _sv_class = sv.BorderStyle

    @property
    def solid(cls):
        return noop / sv.BorderStyle.solid

    @property
    def dashed(cls):
        return noop / sv.BorderStyle.dashed

    @property
    def dotted(cls):
        return noop / sv.BorderStyle.dotted

    @property
    def double(cls):
        return noop / sv.BorderStyle.double

    @property
    def none(cls):
        return noop / sv.BorderStyle.none

    @property
    def collapse(cls):
        return noop / sv.BorderStyle.collapse

    @property
    def separate(cls):
        return noop / sv.BorderStyle.separate


BorderStyle = _BorderStyle()


class _DivideStyle:
    _sv_class = sv.DivideStyle

    @property
    def solid(cls):
        return noop / sv.DivideStyle.solid

    @property
    def dashed(cls):
        return noop / sv.DivideStyle.dashed

    @property
    def dotted(cls):
        return noop / sv.DivideStyle.dotted

    @property
    def double(cls):
        return noop / sv.DivideStyle.double

    @property
    def none(cls):
        return noop / sv.DivideStyle.none

DivideStyle = _DivideStyle()    
    
class _OutlineStyle:
    _sv_class = sv.OutlineStyle

    # @classmethod
    # def __truediv__(cls, valprefix):
    #     return outlineTag / valprefix

    @property
    def none(cls):
        return noop / sv.OutlineStyle.none

    # @property
    # def _(cls):
    #     return noop / sv.OutlineStyle._

    @property
    def dashed(cls):
        return noop / sv.OutlineStyle.dashed

    @property
    def dotted(cls):
        return noop / sv.OutlineStyle.dotted

    @property
    def double(cls):
        return noop / sv.OutlineStyle.double

    @property
    def hidden(cls):
        return noop / sv.OutlineStyle.hidden


OutlineStyle = _OutlineStyle()


class _BoxShadow:
    _sv_class = sv.BoxShadow

    @classmethod
    def __truediv__(cls, valprefix):
        return boxShadowTag / valprefix

    @property
    def sm(cls):
        return noop / sv.BoxShadow.sm

    @property
    def _(cls):
        return noop / sv.BoxShadow._

    @property
    def md(cls):
        return noop / sv.BoxShadow.md

    @property
    def lg(cls):
        return noop / sv.BoxShadow.lg

    @property
    def xl(cls):
        return noop / sv.BoxShadow.xl

    @property
    def xl2(cls):
        return noop / sv.BoxShadow.xl2

    @property
    def none(cls):
        return noop / sv.BoxShadow.none

    @property
    def inner(cls):
        return noop / sv.BoxShadow.inner


BoxShadow = _BoxShadow()


class _Table:
    _sv_class = sv.Table

    @property
    def auto(cls):
        return noop / sv.Table.auto

    @property
    def fixed(cls):
        return noop / sv.Table.fixed


Table = _Table()


class _BoxTopo:
    _sv_class = sv.BoxTopo

    @property
    def bd(cls):
        return noop / sv.BoxTopo.bd

    @property
    def ring(cls):
        return noop / sv.BoxTopo.ring

    @property
    def outline(cls):
        return noop / sv.BoxTopo.outline
    
#     @property
#     def container(cls):
#         return noop / sv.BoxTopo.container


BoxTopo = _BoxTopo()


class _PlacementPosition:
    _sv_class = sv.PlacementPosition

    @property
    def static(cls):
        return noop / sv.PlacementPosition.static

    @property
    def fixed(cls):
        return noop / sv.PlacementPosition.fixed

    @property
    def absolute(cls):
        return noop / sv.PlacementPosition.absolute

    @property
    def relative(cls):
        return noop / sv.PlacementPosition.relative

    @property
    def sticky(cls):
        return noop / sv.PlacementPosition.sticky


PlacementPosition = _PlacementPosition()

class _LayoutVisibility:
    _sv_class = sv.LayoutVisibility
    @property
    def v(cls):
        return noop/sv.LayoutVisibility.v

    
    @property
    def iv(cls):
        return noop/sv.LayoutVisibility.iv

    @property
    def c(cls):
        return noop/sv.LayoutVisibility.c


LayoutVisibility = _LayoutVisibility()

    
class _BoxSizing:
    _sv_class = sv.BoxSizing

    @property
    def b(cls):
        return noop / sv.BoxSizing.b

    @property
    def c(cls):
        return noop / sv.BoxSizing.c


BoxSizing = _BoxSizing()


class _Prose:
    _sv_class = sv.Prose

    @property
    def sm(cls):
        return noop / sv.Prose.sm

    @property
    def _(cls):
        return noop / sv.Prose._

    @property
    def lg(cls):
        return noop / sv.Prose.lg

    @property
    def xl(cls):
        return noop / sv.Prose.xl

    @property
    def xl2(cls):
        return noop / sv.Prose.xl2


Prose = _Prose()


class _GridFlow:
    _sv_class = sv.GridFlow

    @property
    def row(cls):
        return noop / sv.GridFlow.row

    @property
    def col(cls):
        return noop / sv.GridFlow.col

    @property
    def dense(cls):
        return noop / sv.GridFlow.dense
    
    
    @property
    def rowd(cls):
        return noop / sv.GridFlow.rowd

    @property
    def cold(cls):
        return noop / sv.GridFlow.cold


GridFlow = _GridFlow()

class _Whitespace:
    _sv_class = sv.Whitespace

    @property
    def normal(cls):
        return noop / sv.Whitespace.normal

    @property
    def nowrap(cls):
        return noop / sv.Whitespace.nowrap

    @property
    def pre(cls):
        return noop / sv.Whitespace.pre

    @property
    def pre_line(cls):
        return noop / sv.Whitespace.pre_line

    @property
    def pre_wrap(cls):
        return noop / sv.Whitespace.pre_wrap

    @property
    def break_spaces(cls):
        return noop / sv.Whitespace.break_spaces
    
Whitespace = _Whitespace()


class _Overflow:
    _sv_class = sv.Overflow

    @property
    def auto(cls):
        return noop / cls._sv_class.auto

    @property
    def hidden(cls):
        return noop / cls._sv_class.hidden

    @property
    def clip(cls):
        return noop / cls._sv_class.clip

    @property
    def visible(cls):
        return noop / cls._sv_class.visible

    @property
    def scroll(cls):
        return noop / cls._sv_class.scroll

Overflow = _Overflow()


class _OverflowX:
    _sv_class = sv.OverflowX

    @property
    def auto(cls):
        return noop / cls._sv_class.auto

    @property
    def hidden(cls):
        return noop / cls._sv_class.hidden

    @property
    def clip(cls):
        return noop / cls._sv_class.clip

    @property
    def visible(cls):
        return noop / cls._sv_class.visible

    @property
    def scroll(cls):
        return noop / cls._sv_class.scroll

OverflowX = _OverflowX()


class _OverflowY:
    _sv_class = sv.OverflowY

    @property
    def auto(cls):
        return noop / cls._sv_class.auto

    @property
    def hidden(cls):
        return noop / cls._sv_class.hidden

    @property
    def clip(cls):
        return noop / cls._sv_class.clip

    @property
    def visible(cls):
        return noop / cls._sv_class.visible

    @property
    def scroll(cls):
        return noop / cls._sv_class.scroll

OverflowY = _OverflowY()

class _OverscrollBehaviour:
    _sv_class = sv.OverscrollBehaviour

    @property
    def auto(cls):
        return noop/sv.OverscrollBehaviour.auto

    @property
    def contain(cls):
        return noop/sv.OverscrollBehaviour.contain

    @property
    def none(cls):
        return noop/sv.OverscrollBehaviour.none

    @property
    def y_auto(cls):
        return noop/sv.OverscrollBehaviour.y_auto

    @property
    def y_contain(cls):
        return noop/sv.OverscrollBehaviour.y_contain

    @property
    def y_none(cls):
        return noop/sv.OverscrollBehaviour.y_none

    @property
    def x_auto(cls):
        return noop/sv.OverscrollBehaviour.x_auto

    @property
    def x_contain(cls):
        return noop/sv.OverscrollBehaviour.x_contain

    @property
    def x_none(cls):
        return noop/sv.OverscrollBehaviour.x_none

OverscrollBehaviour = _OverscrollBehaviour()


    
class _Transition:
    _sv_class = sv.Transition
    @property
    def none(cls):
        return noop/sv.Transition.none

    @property
    def all(cls):
        return noop/sv.Transition.all

    @property
    def default(cls):
        return noop/sv.Transition.default

    @property
    def colors(cls):
        return noop/sv.Transition.colors

    @property
    def opacity(cls):
        return noop/sv.Transition.opacity

    @property
    def shadow(cls):
        return noop/sv.Transition.shadow

    @property
    def transform(cls):
        return noop/sv.Transition.transform

Transition = _Transition()



class _GridAuto:
    _sv_class = sv.GridAuto

    @property
    def cauto(cls):
        return noop / sv.GridAuto.cauto

    @property
    def cmin(cls):
        return noop / sv.GridAuto.cmin

    @property
    def cmax(cls):
        return noop / sv.GridAuto.cmax

    @property
    def cfr(cls):
        return noop / sv.GridAuto.cfr

    @property
    def rauto(cls):
        return noop / sv.GridAuto.rauto

    @property
    def rmin(cls):
        return noop / sv.GridAuto.rmin

    @property
    def rmax(cls):
        return noop / sv.GridAuto.rmax

    @property
    def rfr(cls):
        return noop / sv.GridAuto.rfr


GridAuto = _GridAuto()

class _ScreenReaders:
    _sv_class = sv.ScreenReaders
    
    @property
    def only(cls):
        return noop / sv.ScreenReaders.only

    @property
    def notonly(cls):
        return noop / sv.ScreenReaders.notonly

ScreenReaders = _ScreenReaders()

class _PointerEvents:
    _sv_class = sv.PointerEvents

    @property
    def none(cls):
        return noop / cls._sv_class.none

    @property
    def auto(cls):
        return noop / cls._sv_class.auto
    
PointerEvents = _PointerEvents()

class _AspectRatio:
    _sv_class = sv.AspectRatio

    @property
    def auto(cls):
        return noop / cls._sv_class.auto

    @property
    def square(cls):
        return noop / cls._sv_class.square

    @property
    def video(cls):
        return noop / cls._sv_class.video

AspectRatio = _AspectRatio()

class _Cursor:
    _sv_class = sv.Cursor

    @property
    def auto(cls):
        return noop / cls._sv_class.auto

    @property
    def default(cls):
        return noop / cls._sv_class.default

    @property
    def pointer(cls):
        return noop / cls._sv_class.pointer

    @property
    def wait(cls):
        return noop / cls._sv_class.wait

    @property
    def text(cls):
        return noop / cls._sv_class.text

    @property
    def move(cls):
        return noop / cls._sv_class.move

    @property
    def help(cls):
        return noop / cls._sv_class.help

    @property
    def not_allowed(cls):
        return noop / cls._sv_class.not_allowed

    @property
    def none(cls):
        return noop / cls._sv_class.none

Cursor = _Cursor()

class _AlignSelf:
    _sv_class = sv.AlignSelf

    @property
    def auto(cls):
        return noop / cls._sv_class.auto

    @property
    def start(cls):
        return noop / cls._sv_class.start

    @property
    def end(cls):
        return noop / cls._sv_class.end

    @property
    def center(cls):
        return noop / cls._sv_class.center

    @property
    def stretch(cls):
        return noop / cls._sv_class.stretch

    @property
    def baseline(cls):
        return noop / cls._sv_class.baseline

AlignSelf = _AlignSelf()

class _BGRepeat:
    _sv_class = sv.BackgroundRepeat

    @property
    def repeat(cls):
        return noop / cls._sv_class.repeat

    @property
    def no_repeat(cls):
        return noop / cls._sv_class.no_repeat

    @property
    def repeat_x(cls):
        return noop / cls._sv_class.repeat_x

    @property
    def repeat_y(cls):
        return noop / cls._sv_class.repeat_y

    @property
    def repeat_round(cls):
        return noop / cls._sv_class.repeat_round

    @property
    def repeat_space(cls):
        return noop / cls._sv_class.repeat_space

BGRepeat = _BGRepeat()


class _LineClamp:
    _sv_class = sv.LineClamp

    @property
    def one(cls):
        return noop / cls._sv_class.one

    @property
    def two(cls):
        return noop / cls._sv_class.two

    @property
    def three(cls):
        return noop / cls._sv_class.three

    @property
    def four(cls):
        return noop / cls._sv_class.four

    @property
    def five(cls):
        return noop / cls._sv_class.five

    @property
    def six(cls):
        return noop / cls._sv_class.six

    @property
    def none(cls):
        return noop / cls._sv_class.none

LineClamp = _LineClamp()

class _Animation:
    _sv_class = sv.Animation

    @property
    def none(cls):
        return noop / cls._sv_class.none

    @property
    def spin(cls):
        return noop / cls._sv_class.spin

    @property
    def ping(cls):
        return noop / cls._sv_class.ping

    @property
    def pulse(cls):
        return noop / cls._sv_class.pulse

    @property
    def bounce(cls):
        return noop / cls._sv_class.bounce

Animation = _Animation()

class _BreakInside:
    _sv_class = sv.BreakInside

    @property
    def auto(cls):
        return noop / cls._sv_class.auto

    @property
    def avoid(cls):
        return noop / cls._sv_class.avoid

    @property
    def avoid_page(cls):
        return noop / cls._sv_class.avoid_page

    @property
    def avoid_column(cls):
        return noop / cls._sv_class.avoid_column

BreakInside =  _BreakInside()



def filter(name):
    if hasattr(current_module, "_" + name):
        if isinstance(getattr(current_module, "_" + name), type):
            return True

    return False


styValueDict = dict(
    [(name, ins) for name, ins in current_module.__dict__.items() if filter(name)]
)
