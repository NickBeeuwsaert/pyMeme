#!/usr/bin/env python

import cairo, sys


class Context(cairo.Context):
	def fill_and_stroke(self, fillColor, strokeColor):
		self.set_source_rgb(*strokeColor);
		path = self.copy_path();
		self.stroke();
		self.append_path(path);
		self.set_source_rgb(*fillColor);
		self.fill()
	def make_text_fit_in_box(self, string, box_size, font_size=48):
		lines = [];
		current_line=[]
		while True:
			self.set_font_size(font_size);
			lines = [];
			current_line=[]
			split_string = string.split()
			while len(split_string) != 0:
				f = split_string[0]
				if self.text_extents(f)[2] > box_size[0]:
					lines+=[split_string.pop(0)]
					continue
				str = " ".join(current_line+[f])
				extents = self.text_extents(str);
				if extents[2] < box_size[0]:
					current_line+=[split_string.pop(0)]
				else:
					lines+=[current_line];
					current_line=[];
			lines += [current_line]
			if len(lines)*font_size < box_size[1]:
				break;
			font_size /= 2
		return (font_size,lines)
	def draw_caption(self, lines, font_size=48):
		self.set_font_size(font_size);
		for line_index in range(len(lines)):
				line = " ".join(lines[line_index])
				extents = self.text_extents(line);
				center = (self.get_target().get_width() - extents[2])/2
				self.move_to(center,font_size+line_index*font_size);
				self.text_path(line);
				# context.fill_and_stroke((1.0,1.0,1.0), (0.0,0.0,0.0));
meme_map = {
"wonka": "templates/wonka.png",
"bad-luck-brian":"templates/bad-luck-brian.png",
"y-u-no":"templates/y-u-no.png",
"first-world-problems":"templates/first-world-problems.png",
"good-guy-greg":"templates/good-guy-greg.png",
"one-does-not-simply":"templates/one-does-not-simply.png",
"futurama-fry":"templates/futurama-fry.png",
"forever-alone": "templates/forever-alone.png",
"conspiracy-keanu":"templates/conspiracy-keanu.png",
"philosoraptor":"templates/philosoraptor.png"


}
def create_meme(which_meme, top, bottom):

	# surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 500,500);
	surface = cairo.ImageSurface.create_from_png(meme_map.get(which_meme,meme_map["forever-alone"]));
	context = Context(surface);
	context.select_font_face("Impact");

	top_caption = context.make_text_fit_in_box(top.upper(), (surface.get_width(),surface.get_height()/3));
	bottom_caption = context.make_text_fit_in_box(bottom.upper(), (surface.get_width(),surface.get_height()/3));
	context.draw_caption(top_caption[1], top_caption[0]);
	context.fill_and_stroke((1.0,1.0,1.0), (0.0,0.0,0.0));

	context.translate(0,surface.get_height()-bottom_caption[0]*len(bottom_caption[1]));
	context.draw_caption(bottom_caption[1], bottom_caption[0]);
	context.fill_and_stroke((1.0,1.0,1.0), (0.0,0.0,0.0));
	return surface
if __name__ == "__main__":
	
	surface = create_meme(sys.argv[1], sys.argv[2],sys.argv[3]);

	surface.write_to_png("out.png");
	
