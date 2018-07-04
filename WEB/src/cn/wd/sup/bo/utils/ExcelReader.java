package cn.wd.sup.bo.utils;

import java.io.InputStream;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFDateUtil;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.poifs.filesystem.POIFSFileSystem;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.DateUtil;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.ss.util.NumberToTextConverter;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

/**
 * 
 * @Package cn.wd.sup.bo.utils
 * @ClassName: ExcelReader
 * @Description: 基础的Excel文件读取类
 * @author WD created.
 * @date 2017年12月3日
 * 
 */
public class ExcelReader {

	Workbook wb = null;
	private static final String EXCEL_XLS = "xls";
	private static final String EXCEL_XLSX = "xlsx";

	protected  ExcelReader(InputStream in, String ext) {
		try {
			if (ext != null && ext.endsWith(EXCEL_XLSX)) { // Excel
									// 2003
				wb = new XSSFWorkbook(in);
			} else if (ext != null && ext.endsWith(EXCEL_XLS)) { // Excel//
										// 2007/2010
				wb = new HSSFWorkbook(in);
			} else {
				POIFSFileSystem fs = new POIFSFileSystem(in);
				wb = new HSSFWorkbook(fs);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	/**
	 * 
	 * @Title: getSheets
	 * @Description: 获取Excel的sheet名称列表
	 * @param is
	 * @return 参数
	 * @return List<String>
	 * @throws
	 */
	public List<String> getSheets() throws Exception {

//		Workbook wb = getWorkbook(is, null);
		List<String> rlst = new ArrayList<String>();

		try {
			Iterator<Sheet> sheets = wb.iterator();
			while (sheets.hasNext()) {
				String sn = sheets.next().getSheetName();
//				System.out.println(sn);
				rlst.add(sn);
			}
			return rlst;
		} finally {
		}
	}

	/**
	 * 
	 * @Title: readTitleRow
	 * @Description: 获取表头信息
	 * @param is
	 * @param sheetName
	 * @param titleRow
	 * @return
	 * @throws Exception
	 *                 参数
	 * @return Map<Integer,String>
	 * @throws
	 */
	public Map<Integer, String> readTitleRow(String sheetName, Integer titleRow) {

		Map<Integer, String> content = new HashMap<Integer, String>();
		try {
			Sheet sheet = null;
			if( sheetName == null || sheetName.length() == 0){
				sheet = wb.getSheetAt(0);
			}else{
				sheet = wb.getSheet(sheetName);
			}

			if (sheet == null) {
				return null;
			}
			// 得到总行数
			Row row = sheet.getRow(titleRow);
			int colNum = row.getPhysicalNumberOfCells();

			for (int i = 0; i < colNum; i++) {
				// 列编号==>列的cell值
				content.put(i, getCellFormatValue(row.getCell(i)).trim());
			}
			return content;
		} catch (Exception e) {
			e.printStackTrace();
			return null;
		}

	}

	/**
	 * 
	 * @Title: readExcelContent
	 * @Description: 读取Excel的内容
	 * @param is
	 * @return 参数
	 * @return Map<Integer,String>
	 * @throws
	 */
	public Map<Integer, String> readExcelContent(String sheetName, Integer titleRow,
					Integer startRow ) {

		Map<Integer, String> content = new HashMap<Integer, String>();
		String str = "";
		try {
			Sheet sheet = null;
			if( sheetName == null || sheetName.length() == 0){
				sheet = wb.getSheetAt(0);
			}else{
				sheet = wb.getSheet(sheetName);
			}
			if (sheet == null) {
				return null;
			}
			// 得到总行数
			int rowNum = sheet.getLastRowNum();
			Row row = sheet.getRow(titleRow);
			int colNum = row.getPhysicalNumberOfCells();
			// 正文内容应该从第二行开始,第一行为表头的标题
			for (int i = startRow; i <= rowNum; i++) {
				row = sheet.getRow(i);
				if (row == null)
					continue;
				int j = 0;
				String dstr = "";
				while (j < colNum) {
					String v = getCellFormatValue(row.getCell(j)).trim();
					dstr += v;
					if( v.length() == 0){
						str += " |";
					}else{
						str += v + "|";
					}
					j++;
				}
				if( dstr.length() > 0){
					content.put(i, str.substring(0, str.length() - 1));
//					System.out.println(str.substring(0, str.length() - 1));
				}
				str = "";
			}
			return content;
		} catch (Exception e) {
			e.printStackTrace();
			return null;
		}
	}

	/**
	 * 根据HSSFCell类型设置数据
	 * 
	 * @param cell
	 * @return
	 */
	private String getCellFormatValue(Cell cell) {
		String cellvalue = "";
		if (cell != null) {
			// 判断当前Cell的Type
			switch (cell.getCellType()) {
			// 如果当前Cell的Type为NUMERIC
			case HSSFCell.CELL_TYPE_NUMERIC:
			case HSSFCell.CELL_TYPE_FORMULA: {
				short format = cell.getCellStyle().getDataFormat();
				if (format == 14 || format == 31 || format == 57 || format == 58) { // excel中的时间格式
					SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
					double value = cell.getNumericCellValue();
					Date date = DateUtil.getJavaDate(value);
					cellvalue = sdf.format(date);
				}
				// 判断当前的cell是否为Date
				else if (HSSFDateUtil.isCellDateFormatted(cell)) { // 先注释日期类型的转换，在实际测试中发现HSSFDateUtil.isCellDateFormatted(cell)只识别2014/02/02这种格式。
					// 如果是Date类型则，取得该Cell的Date值 //
					// 对2014-02-02格式识别不出是日期格式
					Date date = cell.getDateCellValue();
					DateFormat formater = new SimpleDateFormat("yyyy-MM-dd");
					cellvalue = formater.format(date);
				} else { // 如果是纯数字
						// 取得当前Cell的数值
					cellvalue = NumberToTextConverter.toText(cell.getNumericCellValue());
				}
				break;
			}
			// 如果当前Cell的Type为STRIN
			case HSSFCell.CELL_TYPE_STRING:
				// 取得当前的Cell字符串
				cellvalue = cell.getRichStringCellValue().getString();
				break;
			// 默认的Cell值
			default:
				cellvalue = " ";
			}
		} else {
			cellvalue = "";
		}
		return cellvalue;

	}
}
