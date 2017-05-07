#coding=utf-8
import re

username1 = 'zync_134010104033'
username = 'yzu-132003104'

#id = re.match(r'[a-z]*',username)
#print id.group()

#string = '''onclick="window.parent.showPlan(10200000026)'''
#id = re.search(r'window.parent.showPlan\((\d+)\)?',string)
#print id.group()
string = '''<td style="padding-left:10px; color:#333;">搜集就业信息（三）</td>
			                       			                       									<td style="padding-left:10px; color:#888;">已完成（43 / 43）</td>
									<td style="padding-left:10px; color:#888;">
																																								100.0%
																			</td>
									<td style="padding-left:10px; color:#888;">
																																								100.0%
																			</td>
									<td style="padding-left:10px;">
													                        		<a class="a_color" href="javaScript:show(1319);">重看</a>&nbsp;<a class="a_color" href="javaScript:showExercise(1319);">课后习题</a>
			                        				                        </td>
									
											               </tr>
			          		         									                 	 <tr height="50">
			                       <td style="padding-left:10px; color:#333;">心理调适（一）</td>
			                       			                       									<td style="padding-left:10px; color:#888;">已完成（43 / 43）</td>
									<td style="padding-left:10px; color:#888;">
																																								100.0%
																			</td>
									<td style="padding-left:10px; color:#888;">
																																								100.0%
																			</td>
									<td style="padding-left:10px;">
													                        		<a class="a_color" href="javaScript:show(1325);">重看</a>&nbsp;<a class="a_color" href="javaScript:showExercise(1325);">课后习题</a>
			                        				                        </td>
									
											               </tr>
			          		         									                 	 <tr height="50">
			                       <td style="padding-left:10px; color:#333;">心理调适（二）</td>
			                       			                       									<td style="padding-left:10px; color:#888;">已完成（51 / 51）</td>
									<td style="padding-left:10px; color:#888;">
																																								100.0%
																			</td>
									<td style="padding-left:10px; color:#888;">'''







print string.count('观看')
