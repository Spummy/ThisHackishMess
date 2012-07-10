#    Copyright (c) 2012 Connor Sherson
#
#    This file is part of ThisHackishMess
#
#    ThisHackishMess is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame, os
from pygame.locals import *

from hudelement import HudElement
from imageload import loadImageNoAlpha

def splitFrames( image, size ):
	frames = []
	tmpRect = pygame.Rect( (0,0), size )
	for y in xrange( 0, image.get_height(), size[1] ):
		if y + size[1] <= image.get_height():
			for x in xrange( 0, image.get_width(), size[0] ):
				if x + size[0] <= image.get_width():
					tmpRect.topleft = (x, y)
					tmpSurface = image.subsurface( tmpRect )
					frames.append( tmpSurface )
	return frames

class TextBox( HudElement ):
	alpha = False
	sheetFileName = "textboxsheet.png"
	colourKey = pygame.Color( 255, 0, 255 )
	font = pygame.font.Font( os.path.join( "data", "fonts", "Keenton-CCBY.ttf" ), 24 )
	def __init__( self, playState, text, box=None ):
		sheet = loadImageNoAlpha( self.sheetFileName )
		self.originFrames = splitFrames( sheet, (32, 32) )
		if box is None:
			box = pygame.Rect( (0, 350), (800, 250 ) )
		
		img = pygame.Surface( (box.w, box.h) ).convert()
		#img.fill( pygame.Color( 0, 0, 0, 0 ) )

		for x in range( 32, box.w, 32 ):
			img.blit( self.originFrames[1], (x, 0) )
			img.blit( self.originFrames[7], (x, box.h-32) )

		for y in range( 32, box.h, 32 ):
			img.blit( self.originFrames[3], (0, y) )
			img.blit( self.originFrames[5], (box.w-32, y) )

		for x in range( box.x+32, box.w+box.x-32, 32 ):
			for y in range( 32, box.h-32, 32 ):
				img.blit( self.originFrames[4], (x,y) )
		
		img.blit( self.originFrames[0], ( 0, 0 ) )
		img.blit( self.originFrames[2], (box.w-32, 0) )
		img.blit( self.originFrames[6], (0, box.h-32) )
		img.blit( self.originFrames[8], (box.w-32, box.h-32) )
		
		HudElement.__init__( self, playState, box.topleft, img, False )
		self.image.set_colorkey( self.colourKey )
		
	def update( self, dt ):
		HudElement.update( self, dt )