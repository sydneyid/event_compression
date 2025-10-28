#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 18:09:00 2025

@author: sydneydolan
"""

import matplotlib.pyplot as plt
import numpy as np

barWidth = 0.25
raw = [76.29, 75.6, 4.96, 4.96]
zip_meth = [ 68.03, 67.02, 64.14, 64.18]
ous = [ 84.22, 83.78, 81.45, 81.75]

br1 = np.arange(len(raw)) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 

fig, ax = plt.subplots()

ax.bar(br1, raw, color ='#FF0000', width = barWidth, 
        edgecolor ='grey', label ='raw') 

ax.bar(br2, zip_meth, color ='#A6AEBF', width = barWidth, 
        edgecolor ='grey', label ='zip') 

ax.bar(br3, ous, color ='#4C8AEF', width = barWidth, 
        edgecolor ='black',linewidth=1, label ='ours') 

ax.set_xlabel('Scenario', fontsize = 18) 
ax.set_ylabel('Compression Ratio', fontsize = 18) 
ax.set_xticks([r + barWidth for r in range(len(raw))], 
        ['1', '2', '3', '4'])

ax.tick_params(axis='both', which='major', labelsize=16)
ax.tick_params(axis='both', which='minor', labelsize=16)

ax.set_ylim([0,100])
ax.legend(bbox_to_anchor=(0.95, -.17), ncol=3, fontsize=16)



# barWidth = 0.4
# timestamp= [3009462, 1876658, 1292222, 465478, 65351, 1935, 20, 9,2,1]


# br1 = np.arange(len(timestamp)) 

# fig, ax = plt.subplots( figsize=(8, 5.5))

# bars= ax.bar(br1, timestamp, color ='#4C8AEF', width = barWidth, 
#         edgecolor ='grey', label ='raw') 


# ax.set_xlabel('Number of Bits Required for \nTimestamp Representation', fontsize = 18) 
# ax.set_ylabel('Number of Event Timestamps', fontsize = 18) 
# ax.set_xticks([r + barWidth for r in range(len(timestamp))], 
#         ['1', '2', '3', '4','5','6','7','8','9','10'])

# ax.tick_params(axis='both', which='major', labelsize=18)
# ax.tick_params(axis='both', which='minor', labelsize=16)

# ax.bar_label(bars, labels=[f'{v}' for v in timestamp], fontsize=12)
# ax.set_title('Timestamp Bit Analysis',fontsize=20)

# offset_text = ax.yaxis.get_offset_text()

# # Make it larger
# offset_text.set_fontsize(16)


