#coding=utf-8
from bs4 import BeautifulSoup
import re

string = '''搜集就业信息（一）</td>
			                       			                       									<td style="padding-left:10px; color:#888;">已完成（37 / 37）</td>
									<td style="padding-left:10px; color:#888;">
																																								100.0%
																			</td>
									<td style="padding-left:10px; color:#888;">
																																								100.0%
																			</td>
									<td style="padding-left:10px;">
													                        		<a class="a_color" href="javaScript:show(1317);">重看</a>&nbsp;<a class="a_color" href="javaScript:showExercise(1317);">课后习题</a>
			                        				                        </td>
									
											               </tr>
			          		         									                 	 <tr height="50">
			                       <td style="padding-left:10px; color:#333;">搜集就业信息（二）</td>
			                       			                       									<td style="padding-left:10px; color:#888;">已完成（38 / 38）</td>
									<td style="padding-left:10px; color:#888;">
																																								100.0%
																			</td>
									<td style="padding-left:10px; color:#888;">
																																								100.0%
																			</td>
									<td style="padding-left:10px;">
													                        		<a class="a_color" href="javaScript:show(1318);">重看</a>&nbsp;<a class="a_color" href="javaScript:showExercise(1318);">课后习题</a>
			                        				                        </td>
									
											               </tr>
			          		         									                 	 <tr height="50">
			                       <td style="padding-left:10px; color:#333;">搜集就业信息（三）</td>
			                       			                       									<td style="padding-left:10px; color:#888;">已完成（43 / 43）</td>
									<td style="padding-left:10px; color:#888;">
																																								100.0%
																			</td>
									<td style="padding-left:10px; color:#888;">
																																								0.0%
																			</td>
									<td style="padding-left:10px;">
													                        		<a class="a_color" href="javaScript:show(1319);">重看</a>&nbsp;<a class="a_color" href="javaScript:showExercise(1319);">课后习题</a>
			                        				                        </td>
									
											               </tr>
			          		         									                 	 <tr height="50">
			                       <td style="padding-left:10px; color:#333;">搜集就业信息（四）</td>
			                       			                       									<td style="padding-left:10px; color:#888;">已完成（43 / 43）</td>
									<td style="padding-left:10px; color:#888;">
																																								24.0%
																			</td>
									<td style="padding-left:10px; color:#888;">
																																								100.0%
																			</td>
									<td style="padding-left:10px;">'''



#soup = BeautifulSoup(string)
#print soup.select('color')
string1 = re.findall(r'\d+\.0%',string)
mini = min(string1)
if mini == '100.0%':
    print 'hehe'
else:
    print 'hengheng'
