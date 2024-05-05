import cssutils
font_family_css_config_text = """
@font-face {
            font-family: 'Georgia';
            src: url('/fonts/8a1b7122919bb6.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Georgia';
            src: url('/fonts/579b45509a612f.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0370-0377, u+037a-037f, u+0384-038a, u+038c, u+038e-03a1, u+03a3-03ff
    }
@font-face {
            font-family: 'Georgia';
            src: url('/fonts/3aee5c44be9d92.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Georgia';
            src: url('/fonts/2967ec83493cbe.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Roboto';
            src: url('/fonts/926c0ae06a98b4.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0460-052f, u+1c80-1c88, u+20b4, u+2de0-2dff, u+a640-a69f, u+fe2e-fe2f
    }
@font-face {
            font-family: 'Roboto';
            src: url('/fonts/c9f8212e06e524.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Roboto';
            src: url('/fonts/2679101dd24994.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+1f00-1fff
    }
@font-face {
            font-family: 'Roboto';
            src: url('/fonts/a22d46730be0e7.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0370-0377, u+037a-037f, u+0384-038a, u+038c, u+038e-03a1, u+03a3-03ff
    }
@font-face {
            font-family: 'Roboto';
            src: url('/fonts/c23d414613ba51.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Roboto';
            src: url('/fonts/32f669456fb608.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Roboto';
            src: url('/fonts/23a6e35415e08c.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Lato';
            src: url('/fonts/396454295bc96a.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Lato';
            src: url('/fonts/61972548003c12.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Montserrat';
            src: url('/fonts/9a5e88221c1441.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0460-052f, u+1c80-1c88, u+20b4, u+2de0-2dff, u+a640-a69f, u+fe2e-fe2f
    }
@font-face {
            font-family: 'Montserrat';
            src: url('/fonts/790ce274e74fe7.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Montserrat';
            src: url('/fonts/44ccda2181a45f.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Montserrat';
            src: url('/fonts/f78e456bbb054e.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Montserrat';
            src: url('/fonts/c8e6370d8770cc.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Raleway';
            src: url('/fonts/5f0eca43426b0e.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0460-052f, u+1c80-1c88, u+20b4, u+2de0-2dff, u+a640-a69f, u+fe2e-fe2f
    }
@font-face {
            font-family: 'Raleway';
            src: url('/fonts/5607116fbd5351.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Raleway';
            src: url('/fonts/a42da193c185e2.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Raleway';
            src: url('/fonts/97b0637c3a7c51.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Raleway';
            src: url('/fonts/c80be815d0254c.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Merriweather';
            src: url('/fonts/25c8af6a067b8e.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0460-052f, u+1c80-1c88, u+20b4, u+2de0-2dff, u+a640-a69f, u+fe2e-fe2f
    }
@font-face {
            font-family: 'Merriweather';
            src: url('/fonts/08499ee4ef6f97.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Merriweather';
            src: url('/fonts/651c15726366a8.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Merriweather';
            src: url('/fonts/9d320d3af2a842.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Merriweather';
            src: url('/fonts/33001a2ff07512.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Georgia';
            src: url('/fonts/8a1b7122919bb6.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Georgia';
            src: url('/fonts/579b45509a612f.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0370-0377, u+037a-037f, u+0384-038a, u+038c, u+038e-03a1, u+03a3-03ff
    }
@font-face {
            font-family: 'Georgia';
            src: url('/fonts/3aee5c44be9d92.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Georgia';
            src: url('/fonts/2967ec83493cbe.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Playfair Display';
            src: url('/fonts/8ac507d6d78b16.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Playfair Display';
            src: url('/fonts/4737738d09caf6.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Playfair Display';
            src: url('/fonts/c4f5fc5b0b1521.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Playfair Display';
            src: url('/fonts/f4c28d6283cfc7.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Libre Baskerville';
            src: url('/fonts/4449c09f6605f6.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Libre Baskerville';
            src: url('/fonts/b082f8970eca86.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Crimson Text';
            src: url('/fonts/50088cc30bf79a.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Crimson Text';
            src: url('/fonts/6ffc02b6c5fc9e.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Crimson Text';
            src: url('/fonts/e10a82d0c6f863.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Lora';
            src: url('/fonts/672839ea976b49.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0460-052f, u+1c80-1c88, u+20b4, u+2de0-2dff, u+a640-a69f, u+fe2e-fe2f
    }
@font-face {
            font-family: 'Lora';
            src: url('/fonts/f09a8cd7af17a2.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Lora';
            src: url('/fonts/8f42a5b971b9a6.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0302-0303, u+0305, u+0307-0308, u+0330, u+0391-03a1, u+03a3-03a9, u+03b1-03c9, u+03d1, u+03d5-03d6, u+03f0-03f1, u+03f4-03f5, u+2034-2037, u+2057, u+20d0-20dc, u+20e1, u+20e5-20ef, u+2102, u+210a-210e, u+2110-2112, u+2115, u+2119-211d, u+2124, u+2128, u+212c-212d, u+212f-2131, u+2133-2138, u+213c-2140, u+2145-2149, u+2190, u+2192, u+2194-21ae, u+21b0-21e5, u+21f1-21f2, u+21f4-2211, u+2213-2214, u+2216-22ff, u+2308-230b, u+2310, u+2319, u+231c-2321, u+2336-237a, u+237c, u+2395, u+239b-23b6, u+23d0, u+23dc-23e1, u+2474-2475, u+25af, u+25b3, u+25b7, u+25bd, u+25c1, u+25ca, u+25cc, u+25fb, u+266d-266f, u+27c0-27ff, u+2900-2aff, u+2b0e-2b11, u+2b30-2b4c, u+2bfe, u+ff5b, u+ff5d, u+1d400-1d7ff, u+1ee00-1eeff
    }
@font-face {
            font-family: 'Lora';
            src: url('/fonts/8fec3a4f7d504a.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0001-000c, u+000e-001f, u+007f-009f, u+20dd-20e0, u+20e2-20e4, u+2150-218f, u+2190, u+2192, u+2194-2199, u+21af, u+21e6-21f0, u+21f3, u+2218-2219, u+2299, u+22c4-22c6, u+2300-243f, u+2440-244a, u+2460-24ff, u+25a0-27bf, u+2800-28ff, u+2921-2922, u+2981, u+29bf, u+29eb, u+2b00-2bff, u+4dc0-4dff, u+fff9-fffb, u+10140-1018e, u+10190-1019c, u+101a0, u+101d0-101fd, u+102e0-102fb, u+10e60-10e7e, u+1d2c0-1d2d3, u+1d2e0-1d37f, u+1f000-1f0ff, u+1f100-1f1ad, u+1f1e6-1f1ff, u+1f30d-1f30f, u+1f315, u+1f31c, u+1f31e, u+1f320-1f32c, u+1f336, u+1f378, u+1f37d, u+1f382, u+1f393-1f39f, u+1f3a7-1f3a8, u+1f3ac-1f3af, u+1f3c2, u+1f3c4-1f3c6, u+1f3ca-1f3ce, u+1f3d4-1f3e0, u+1f3ed, u+1f3f1-1f3f3, u+1f3f5-1f3f7, u+1f408, u+1f415, u+1f41f, u+1f426, u+1f43f, u+1f441-1f442, u+1f444, u+1f446-1f449, u+1f44c-1f44e, u+1f453, u+1f46a, u+1f47d, u+1f4a3, u+1f4b0, u+1f4b3, u+1f4b9, u+1f4bb, u+1f4bf, u+1f4c8-1f4cb, u+1f4d6, u+1f4da, u+1f4df, u+1f4e3-1f4e6, u+1f4ea-1f4ed, u+1f4f7, u+1f4f9-1f4fb, u+1f4fd-1f4fe, u+1f503, u+1f507-1f50b, u+1f50d, u+1f512-1f513, u+1f53e-1f54a, u+1f54f-1f5fa, u+1f610, u+1f650-1f67f, u+1f687, u+1f68d, u+1f691, u+1f694, u+1f698, u+1f6ad, u+1f6b2, u+1f6b9-1f6ba, u+1f6bc, u+1f6c6-1f6cf, u+1f6d3-1f6d7, u+1f6e0-1f6ea, u+1f6f0-1f6f3, u+1f6f7-1f6fc, u+1f700-1f7ff, u+1f800-1f80b, u+1f810-1f847, u+1f850-1f859, u+1f860-1f887, u+1f890-1f8ad, u+1f8b0-1f8b1, u+1f900-1f90b, u+1f93b, u+1f946, u+1f984, u+1f996, u+1f9e9, u+1fa00-1fa6f, u+1fa70-1fa7c, u+1fa80-1fa88, u+1fa90-1fabd, u+1fabf-1fac5, u+1face-1fadb, u+1fae0-1fae8, u+1faf0-1faf8, u+1fb00-1fbff
    }
@font-face {
            font-family: 'Lora';
            src: url('/fonts/e520f729d1546f.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Lora';
            src: url('/fonts/85027f97e4d208.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Lora';
            src: url('/fonts/c49018d97d17ff.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Cardo';
            src: url('/fonts/9bca996be8685c.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+1f00-1fff
    }
@font-face {
            font-family: 'Cardo';
            src: url('/fonts/281af1961a7620.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0370-0377, u+037a-037f, u+0384-038a, u+038c, u+038e-03a1, u+03a3-03ff
    }
@font-face {
            font-family: 'Cardo';
            src: url('/fonts/915d9c5c6fcfa4.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Cardo';
            src: url('/fonts/7d91177d4e3ddd.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Helvetica';
            src: url('/fonts/15d7f8ededd8df.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Helvetica';
            src: url('/fonts/f380bd7a1cb1ed.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Helvetica';
            src: url('/fonts/6b77555fd1dbd8.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Open Sans';
            src: url('/fonts/2e714829916184.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0460-052f, u+1c80-1c88, u+20b4, u+2de0-2dff, u+a640-a69f, u+fe2e-fe2f
    }
@font-face {
            font-family: 'Open Sans';
            src: url('/fonts/10626a7dda57a6.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Open Sans';
            src: url('/fonts/2a7ceca7ac6630.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+1f00-1fff
    }
@font-face {
            font-family: 'Open Sans';
            src: url('/fonts/1263c544b3d6c7.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0370-0377, u+037a-037f, u+0384-038a, u+038c, u+038e-03a1, u+03a3-03ff
    }
@font-face {
            font-family: 'Open Sans';
            src: url('/fonts/8d10fe849967da.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0590-05ff, u+200c-2010, u+20aa, u+25cc, u+fb1d-fb4f
    }
@font-face {
            font-family: 'Open Sans';
            src: url('/fonts/5d31f96496f009.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0302-0303, u+0305, u+0307-0308, u+0330, u+0391-03a1, u+03a3-03a9, u+03b1-03c9, u+03d1, u+03d5-03d6, u+03f0-03f1, u+03f4-03f5, u+2034-2037, u+2057, u+20d0-20dc, u+20e1, u+20e5-20ef, u+2102, u+210a-210e, u+2110-2112, u+2115, u+2119-211d, u+2124, u+2128, u+212c-212d, u+212f-2131, u+2133-2138, u+213c-2140, u+2145-2149, u+2190, u+2192, u+2194-21ae, u+21b0-21e5, u+21f1-21f2, u+21f4-2211, u+2213-2214, u+2216-22ff, u+2308-230b, u+2310, u+2319, u+231c-2321, u+2336-237a, u+237c, u+2395, u+239b-23b6, u+23d0, u+23dc-23e1, u+2474-2475, u+25af, u+25b3, u+25b7, u+25bd, u+25c1, u+25ca, u+25cc, u+25fb, u+266d-266f, u+27c0-27ff, u+2900-2aff, u+2b0e-2b11, u+2b30-2b4c, u+2bfe, u+ff5b, u+ff5d, u+1d400-1d7ff, u+1ee00-1eeff
    }
@font-face {
            font-family: 'Open Sans';
            src: url('/fonts/b13474356175b4.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0001-000c, u+000e-001f, u+007f-009f, u+20dd-20e0, u+20e2-20e4, u+2150-218f, u+2190, u+2192, u+2194-2199, u+21af, u+21e6-21f0, u+21f3, u+2218-2219, u+2299, u+22c4-22c6, u+2300-243f, u+2440-244a, u+2460-24ff, u+25a0-27bf, u+2800-28ff, u+2921-2922, u+2981, u+29bf, u+29eb, u+2b00-2bff, u+4dc0-4dff, u+fff9-fffb, u+10140-1018e, u+10190-1019c, u+101a0, u+101d0-101fd, u+102e0-102fb, u+10e60-10e7e, u+1d2c0-1d2d3, u+1d2e0-1d37f, u+1f000-1f0ff, u+1f100-1f1ad, u+1f1e6-1f1ff, u+1f30d-1f30f, u+1f315, u+1f31c, u+1f31e, u+1f320-1f32c, u+1f336, u+1f378, u+1f37d, u+1f382, u+1f393-1f39f, u+1f3a7-1f3a8, u+1f3ac-1f3af, u+1f3c2, u+1f3c4-1f3c6, u+1f3ca-1f3ce, u+1f3d4-1f3e0, u+1f3ed, u+1f3f1-1f3f3, u+1f3f5-1f3f7, u+1f408, u+1f415, u+1f41f, u+1f426, u+1f43f, u+1f441-1f442, u+1f444, u+1f446-1f449, u+1f44c-1f44e, u+1f453, u+1f46a, u+1f47d, u+1f4a3, u+1f4b0, u+1f4b3, u+1f4b9, u+1f4bb, u+1f4bf, u+1f4c8-1f4cb, u+1f4d6, u+1f4da, u+1f4df, u+1f4e3-1f4e6, u+1f4ea-1f4ed, u+1f4f7, u+1f4f9-1f4fb, u+1f4fd-1f4fe, u+1f503, u+1f507-1f50b, u+1f50d, u+1f512-1f513, u+1f53e-1f54a, u+1f54f-1f5fa, u+1f610, u+1f650-1f67f, u+1f687, u+1f68d, u+1f691, u+1f694, u+1f698, u+1f6ad, u+1f6b2, u+1f6b9-1f6ba, u+1f6bc, u+1f6c6-1f6cf, u+1f6d3-1f6d7, u+1f6e0-1f6ea, u+1f6f0-1f6f3, u+1f6f7-1f6fc, u+1f700-1f7ff, u+1f800-1f80b, u+1f810-1f847, u+1f850-1f859, u+1f860-1f887, u+1f890-1f8ad, u+1f8b0-1f8b1, u+1f900-1f90b, u+1f93b, u+1f946, u+1f984, u+1f996, u+1f9e9, u+1fa00-1fa6f, u+1fa70-1fa7c, u+1fa80-1fa88, u+1fa90-1fabd, u+1fabf-1fac5, u+1face-1fadb, u+1fae0-1fae8, u+1faf0-1faf8, u+1fb00-1fbff
    }
@font-face {
            font-family: 'Open Sans';
            src: url('/fonts/7e47d72c384e6c.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Open Sans';
            src: url('/fonts/4bff157df00be8.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Open Sans';
            src: url('/fonts/01681928f65064.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Avenir';
            src: url('/fonts/418e1c67b56462.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Avenir';
            src: url('/fonts/061f31e6ba3334.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Nunito Sans';
            src: url('/fonts/ff6862b44cf2e6.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0460-052f, u+1c80-1c88, u+20b4, u+2de0-2dff, u+a640-a69f, u+fe2e-fe2f
    }
@font-face {
            font-family: 'Nunito Sans';
            src: url('/fonts/72577aad76a527.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Nunito Sans';
            src: url('/fonts/469edde29933a4.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Nunito Sans';
            src: url('/fonts/8bd5de6efa6ef0.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Nunito Sans';
            src: url('/fonts/7dcb6b217dbb61.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Source Sans Pro';
            src: url('/fonts/9289a5077b045f.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0460-052f, u+1c80-1c88, u+20b4, u+2de0-2dff, u+a640-a69f, u+fe2e-fe2f
    }
@font-face {
            font-family: 'Source Sans Pro';
            src: url('/fonts/09fbff3207d5cb.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Source Sans Pro';
            src: url('/fonts/14e0b4671149aa.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+1f00-1fff
    }
@font-face {
            font-family: 'Source Sans Pro';
            src: url('/fonts/b4754c99329f99.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0370-0377, u+037a-037f, u+0384-038a, u+038c, u+038e-03a1, u+03a3-03ff
    }
@font-face {
            font-family: 'Source Sans Pro';
            src: url('/fonts/4d0611918cfc0b.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Source Sans Pro';
            src: url('/fonts/67f6d75e377bb8.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Source Sans Pro';
            src: url('/fonts/b63baf315c4c13.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Roboto Condensed';
            src: url('/fonts/26001054e98e95.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0460-052f, u+1c80-1c88, u+20b4, u+2de0-2dff, u+a640-a69f, u+fe2e-fe2f
    }
@font-face {
            font-family: 'Roboto Condensed';
            src: url('/fonts/051b49f31d013f.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Roboto Condensed';
            src: url('/fonts/7f8c8b2abca18c.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+1f00-1fff
    }
@font-face {
            font-family: 'Roboto Condensed';
            src: url('/fonts/4c0dbaf381e4ba.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0370-0377, u+037a-037f, u+0384-038a, u+038c, u+038e-03a1, u+03a3-03ff
    }
@font-face {
            font-family: 'Roboto Condensed';
            src: url('/fonts/06efa609a81484.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Roboto Condensed';
            src: url('/fonts/a85fa8569bf501.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Roboto Condensed';
            src: url('/fonts/15db805902ac91.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Courier New';
            src: url('/fonts/85218957a7e942.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Roboto Mono';
            src: url('/fonts/d54b2ba21351a1.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0460-052f, u+1c80-1c88, u+20b4, u+2de0-2dff, u+a640-a69f, u+fe2e-fe2f
    }
@font-face {
            font-family: 'Roboto Mono';
            src: url('/fonts/6c063b81647790.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Roboto Mono';
            src: url('/fonts/505d1c18d708be.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0370-0377, u+037a-037f, u+0384-038a, u+038c, u+038e-03a1, u+03a3-03ff
    }
@font-face {
            font-family: 'Roboto Mono';
            src: url('/fonts/ee29820393d3a8.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Roboto Mono';
            src: url('/fonts/f49aa67b134b59.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Roboto Mono';
            src: url('/fonts/f4a035ff580232.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Inconsolata';
            src: url('/fonts/a33d4a8a2f6b22.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Inconsolata';
            src: url('/fonts/239ad3c74ea689.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Inconsolata';
            src: url('/fonts/b25a0d2b56727f.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Source Code Pro';
            src: url('/fonts/8029fc9a46d418.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0460-052f, u+1c80-1c88, u+20b4, u+2de0-2dff, u+a640-a69f, u+fe2e-fe2f
    }
@font-face {
            font-family: 'Source Code Pro';
            src: url('/fonts/c8876a5b41d7f7.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Source Code Pro';
            src: url('/fonts/87bca4d219d42d.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+1f00-1fff
    }
@font-face {
            font-family: 'Source Code Pro';
            src: url('/fonts/9078e234560aea.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0370-0377, u+037a-037f, u+0384-038a, u+038c, u+038e-03a1, u+03a3-03ff
    }
@font-face {
            font-family: 'Source Code Pro';
            src: url('/fonts/6572ca8715fada.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Source Code Pro';
            src: url('/fonts/b3df9f7a989cf5.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Source Code Pro';
            src: url('/fonts/e9dea707dbc6d0.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Pacifico';
            src: url('/fonts/592adc6d3939dd.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0460-052f, u+1c80-1c88, u+20b4, u+2de0-2dff, u+a640-a69f, u+fe2e-fe2f
    }
@font-face {
            font-family: 'Pacifico';
            src: url('/fonts/a44b497752e567.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Pacifico';
            src: url('/fonts/6e24e2aab3f164.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Pacifico';
            src: url('/fonts/728427bcfa1a89.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Pacifico';
            src: url('/fonts/41a9731f9e6be8.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Raleway Dots';
            src: url('/fonts/ec37c87007c63d.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Raleway Dots';
            src: url('/fonts/51674cf7b055d3.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Sacramento';
            src: url('/fonts/ef506336005818.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Sacramento';
            src: url('/fonts/1bfe28961ac62e.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Anton';
            src: url('/fonts/cb4ab79ce806a5.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Anton';
            src: url('/fonts/dc4f9d033518e1.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Anton';
            src: url('/fonts/953917c1a37658.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Cinzel';
            src: url('/fonts/c75e134b978ee6.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Cinzel';
            src: url('/fonts/bdaff11cc1e0f7.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Dancing Script';
            src: url('/fonts/7d2a221fa2adf9.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Dancing Script';
            src: url('/fonts/889afa41c2b91c.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Dancing Script';
            src: url('/fonts/a82c76c75647a5.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Great Vibes';
            src: url('/fonts/5d8797ba292284.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Great Vibes';
            src: url('/fonts/ca1c2c75d71ef8.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Great Vibes';
            src: url('/fonts/e1cb96a619fabe.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Kaushan Script';
            src: url('/fonts/7c7074d511ae5f.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Kaushan Script';
            src: url('/fonts/e542db0cd0cc07.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Josefin Sans';
            src: url('/fonts/30009c4cf7d78a.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Josefin Sans';
            src: url('/fonts/b9d5e82358642c.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Josefin Sans';
            src: url('/fonts/893dcc06d696f0.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Abril Fatface';
            src: url('/fonts/b3aabda913e7d9.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Abril Fatface';
            src: url('/fonts/d245a43248031e.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Lobster';
            src: url('/fonts/1629eae42a9728.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0460-052f, u+1c80-1c88, u+20b4, u+2de0-2dff, u+a640-a69f, u+fe2e-fe2f
    }
@font-face {
            font-family: 'Lobster';
            src: url('/fonts/f8fd3e09de0054.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Lobster';
            src: url('/fonts/1b85dcd20d4fcd.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Lobster';
            src: url('/fonts/4cf524fad514c5.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Lobster';
            src: url('/fonts/a40d5c87124c1e.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Shadows Into Light';
            src: url('/fonts/27d9d1e2378f5d.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Patrick Hand';
            src: url('/fonts/d4eb1fa33c4d7e.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Patrick Hand';
            src: url('/fonts/7b2d6b1a1f130f.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Patrick Hand';
            src: url('/fonts/ffb4e9e8a8f5d2.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Permanent Marker';
            src: url('/fonts/58ea338e63c56f.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Indie Flower';
            src: url('/fonts/0e2a5ce54c666b.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Satisfy';
            src: url('/fonts/11c7ed08741340.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Inter';
            src: url('/fonts/c9792b88a0dfea.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0460-052f, u+1c80-1c88, u+20b4, u+2de0-2dff, u+a640-a69f, u+fe2e-fe2f
    }
@font-face {
            font-family: 'Inter';
            src: url('/fonts/5d63823732fdec.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Inter';
            src: url('/fonts/e200bec3ca77ea.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+1f00-1fff
    }
@font-face {
            font-family: 'Inter';
            src: url('/fonts/d6b9a84e3a5761.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0370-0377, u+037a-037f, u+0384-038a, u+038c, u+038e-03a1, u+03a3-03ff
    }
@font-face {
            font-family: 'Inter';
            src: url('/fonts/430c6fe10edc7d.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Inter';
            src: url('/fonts/39a99a08adf19a.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Inter';
            src: url('/fonts/fc145636489a0c.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Poppins';
            src: url('/fonts/78e1717688c676.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Poppins';
            src: url('/fonts/fa94c49f76f8dc.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }
@font-face {
            font-family: 'Proxima Nova';
            src: url('/fonts/d908d9273d2a95.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0301, u+0400-045f, u+0490-0491, u+04b0-04b1, u+2116
    }
@font-face {
            font-family: 'Proxima Nova';
            src: url('/fonts/66b981f526f336.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0102-0103, u+0110-0111, u+0128-0129, u+0168-0169, u+01a0-01a1, u+01af-01b0, u+0300-0301, u+0303-0304, u+0308-0309, u+0323, u+0329, u+1ea0-1ef9, u+20ab
    }
@font-face {
            font-family: 'Proxima Nova';
            src: url('/fonts/c7b3a94b941a42.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0100-02af, u+0304, u+0308, u+0329, u+1e00-1e9f, u+1ef2-1eff, u+2020, u+20a0-20ab, u+20ad-20c0, u+2113, u+2c60-2c7f, u+a720-a7ff
    }
@font-face {
            font-family: 'Proxima Nova';
            src: url('/fonts/889009d5e4bfc3.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
            unicode-range: u+0000-00ff, u+0131, u+0152-0153, u+02bb-02bc, u+02c6, u+02da, u+02dc, u+0304, u+0308, u+0329, u+2000-206f, u+2074, u+20ac, u+2122, u+2191, u+2193, u+2212, u+2215, u+feff, u+fffd
    }

@font-face {
  font-family: 'Geist';
  src: url('/fonts/Geist-Regular.woff2') format('woff2'),
       url('/fonts/Geist-Regular.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'Geist';
  src: url('/fonts/Geist-Light.woff2') format('woff2'),
       url('/fonts/Geist-Light.woff') format('woff');
  font-weight: 300;
  font-style: normal;
}

@font-face {
  font-family: 'Geist';
  src: url('/fonts/Geist-Medium.woff2') format('woff2'),
       url('/fonts/Geist-Medium.woff') format('woff');
  font-weight: 500;
  font-style: normal;
}

@font-face {
  font-family: 'Geist';
  src: url('/fonts/Geist-SemiBold.woff2') format('woff2'),
       url('/fonts/Geist-SemiBold.woff') format('woff');
  font-weight: 600;
  font-style: normal;
}

@font-face {
  font-family: 'Geist';
  src: url('/fonts/Geist-Bold.woff2') format('woff2'),
       url('/fonts/Geist-Bold.woff') format('woff');
  font-weight: bold;
  font-style: normal;
}

@font-face {
  font-family: 'Geist';
  src: url('/fonts/Geist-Black.woff2') format('woff2'),
       url('/fonts/Geist-Black.woff') format('woff');
  font-weight: 900;
  font-style: normal;
}

"""

def group_fonts_by_family(css_text):
    parser = cssutils.CSSParser()
    stylesheet = parser.parseString(css_text)
    fonts_by_family = {}
    
    for rule in stylesheet:
        if rule.type == rule.FONT_FACE_RULE:
            # cssutils makes the quotes part of the font-family
            # we need to strip it out
            font_family = rule.style['font-family'].strip("'\"")

            fonts_by_family.setdefault(font_family, []).append(rule.cssText)
            
    return fonts_by_family

fonts_by_family = group_fonts_by_family(font_family_css_config_text)

# for font_family, rules in fonts_by_family.items():
#     print(f"Font Family: {font_family}")
#     for rule in rules:
#         print(f"  {rule}")
#     print("-" * 50)
